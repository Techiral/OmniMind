import os
import json

def load_config(config_path=None):
    """Load MCP server config from a file or environment variable."""
    if not config_path:
        config_path = os.getenv("THEAILANGUAGE_CONFIG", "theailanguage_config.json")
        if not os.path.isabs(config_path):
            config_path = os.path.join(os.path.dirname(__file__), "..", config_path)

    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        raise FileNotFoundError(f"Failed to load config at '{config_path}': {e}")