# Add your own server to OmniMind
from omnimind import OmniMind

agent = OmniMind()
agent.add_server("my_server", command="python", args=["my_server.py"])
agent.run()  # Your server’s live!