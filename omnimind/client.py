import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from contextlib import AsyncExitStack
import os
import json
from .config import load_config
from .utils import CustomEncoder

class OmniMind:
    def __init__(self, config_path=None, api_key=None):
        """Initialize OmniMind with a config file or default settings."""
        self.config = load_config(config_path)
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            max_retries=2,
            google_api_key=api_key or os.getenv("GOOGLE_API_KEY")
        )
        self.tools = []
        self.agent = None

    async def _connect_servers(self):
        """Connect to all MCP servers and load tools."""
        mcp_servers = self.config.get("mcpServers", {})
        if not mcp_servers:
            raise ValueError("No MCP servers defined in config.")

        async with AsyncExitStack() as stack:
            for name, info in mcp_servers.items():
                print(f"🔗 Connecting to {name}...")
                params = StdioServerParameters(command=info["command"], args=info["args"])
                try:
                    read, write = await stack.enter_async_context(stdio_client(params))
                    session = await stack.enter_async_context(ClientSession(read, write))
                    await session.initialize()
                    server_tools = await load_mcp_tools(session)
                    self.tools.extend(server_tools)
                    print(f"✅ Loaded {len(server_tools)} tools from {name}.")
                except Exception as e:
                    print(f"❌ Failed to connect to {name}: {e}")

        if not self.tools:
            raise RuntimeError("No tools loaded from any server.")
        self.agent = create_react_agent(self.llm, self.tools)

    def add_server(self, name, command, args, env=None):
        """Add a new MCP server programmatically."""
        self.config["mcpServers"][name] = {"command": command, "args": args}
        if env:
            self.config["mcpServers"][name]["env"] = env

    async def _run(self):
        """Run the interactive chat loop."""
        await self._connect_servers()
        print("🚀 OmniMind Ready! Type 'quit' to exit.")
        while True:
            query = input("\nQuery: ").strip()
            if query.lower() == "quit":
                break
            response = await self.agent.ainvoke({"messages": query})
            print("\nResponse:")
            print(json.dumps(response, indent=2, cls=CustomEncoder))

    def run(self):
        """Synchronous wrapper for running the agent."""
        asyncio.run(self._run())

    async def invoke(self, query):
        """Invoke the agent with a query and return the response."""
        if not self.agent:
            await self._connect_servers()
        return await self.agent.ainvoke({"messages": query})