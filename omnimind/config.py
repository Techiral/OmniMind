import os
import json

def load_config(config_path):
    """Load MCP server config from a user-provided file."""
    if not config_path:
        raise ValueError("A config file path must be provided to use OmniMind")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at '{config_path}'")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        if not config.get("mcpServers"):
            raise ValueError("Config file must contain 'mcpServers' key with server definitions")
        return config
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file at '{config_path}': {e}")
    except Exception as e:
        raise FileNotFoundError(f"Failed to load config at '{config_path}': {e}")