# client.py

# ─────────────────────────────────────────────────────────────────────────────
# Suppress Windows asyncio “unclosed transport” ResourceWarning at shutdown
# ─────────────────────────────────────────────────────────────────────────────
import warnings
warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed transport.*")

import asyncio
import os
import logging
import signal
import sys
import atexit
from contextlib import AsyncExitStack, suppress
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from .config import load_config
from .utils import CustomEncoder

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

_active_instances = set()

class OmniMind:
    def __init__(self, config_path, api_key=None):
        self.config = load_config(config_path)
        google_api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not google_api_key:
            raise ValueError("GOOGLE_API_KEY must be provided via env or api_key")
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            max_retries=2,
            google_api_key=google_api_key
        )
        self.tools = []
        self.agent = None
        self.sessions = {}
        self.exit_stack = None
        self.is_connected = False
        self._transports = []

        _active_instances.add(self)
        for sig in (signal.SIGINT, signal.SIGTERM):
            signal.signal(sig, lambda *_: self._emergency_cleanup())
        atexit.register(self._ensure_cleanup)

    def _emergency_cleanup(self):
        if self.is_connected:
            logger.warning("Emergency cleanup…")
            try:
                loop = asyncio.new_event_loop()
                loop.run_until_complete(self.close())
                loop.close()
            except Exception as e:
                logger.error(f"Error during emergency cleanup: {e}")
        _active_instances.discard(self)

    def _ensure_cleanup(self):
        if self.is_connected:
            logger.warning("Exit cleanup…")
            try:
                loop = asyncio.new_event_loop()
                loop.run_until_complete(self.close())
                loop.close()
            except Exception as e:
                logger.error(f"Error during cleanup: {e}")
        _active_instances.discard(self)

    async def _connect_servers(self):
        if self.is_connected:
            return

        servers = self.config.get("mcpServers", {})
        if not servers:
            raise ValueError("No MCP servers in config")

        self.exit_stack = AsyncExitStack()
        
        try:
            for name, info in servers.items():
                logger.info(f"Connecting: {name}")

                env = os.environ.copy()
                env.update(info.get("env", {}))

                params = StdioServerParameters(
                    command=info["command"],
                    args=info["args"],
                    env=env
                )

                try:
                    read, write = await self.exit_stack.enter_async_context(
                        stdio_client(params)
                    )
                    for stream in (read, write):
                        tr = getattr(stream, "_transport", None)
                        if tr:
                            self._transports.append(tr)
                            proc = getattr(tr, "_proc", None)
                            if proc:
                                self._transports.append(proc)

                    session = await self.exit_stack.enter_async_context(
                        ClientSession(read, write)
                    )
                    await session.initialize()
                    logger.info(f"{name} initialized")

                    tools = await load_mcp_tools(session)
                    if tools:
                        self.tools.extend(tools)
                        logger.info(f"{len(tools)} tools from {name}")
                    else:
                        logger.warning(f"No tools on {name}")

                    self.sessions[name] = session

                except Exception as e:
                    logger.error(f"{name} failed: {e}")

            if not self.tools:
                raise RuntimeError("No tools loaded")

            self.agent = create_react_agent(self.llm, self.tools)
            self.is_connected = True
            logger.info(f"Agent ready with: {self.format_tools(self.tools)}")

        except Exception:
            await self.exit_stack.aclose()
            raise

    async def close(self):
        if not self.is_connected:
            return

        logger.info("Closing connections…")
        self.sessions.clear()
        self.tools.clear()
        self.agent = None

        if self.exit_stack:
            with suppress(Exception):
                await self.exit_stack.aclose()
            self.exit_stack = None

        for obj in self._transports:
            with suppress(Exception):
                if hasattr(obj, "terminate"):
                    obj.terminate()
                if hasattr(obj, "close"):
                    obj.close()
        self._transports.clear()

        self.is_connected = False
        logger.info("All cleaned up")

    async def invoke(self, query: str):
        if not self.is_connected:
            await self._connect_servers()
        return await self.agent.ainvoke({"messages": [HumanMessage(content=query)]})

    async def __aenter__(self):
        await self._connect_servers()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    def format_tools(self, tools):
        return "\n".join([f"'{tool.name}'" for tool in tools])

    def run(self):
        async def _loop():
            await self._connect_servers()
            print("Ready! Type 'quit' to exit.")
            while True:
                q = input("Query: ").strip()
                if q.lower() == "quit":
                    break
                resp = await self.agent.ainvoke({"messages": [HumanMessage(content=q)]})
                print(json.dumps(resp, indent=2, cls=CustomEncoder))
            await self.close()

        try:
            asyncio.run(_loop())
        except KeyboardInterrupt:
            asyncio.run(self.close())
        except Exception as e:
            logger.error(f"Error during run: {e}")