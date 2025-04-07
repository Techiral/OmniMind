# How to Use OmniMind

Welcome to OmniMind! This Python library makes it easy and fun to work with MCP (Model Context Protocol) and AI. Whether you’re a beginner who’s never coded before, a developer building cool projects, a solopreneur saving time, or a business owner adding smart tools, OmniMind is your starting point. It’s free, simple to use, and connects you to MCP servers—think of them as helpers that do tasks like fetching web info, managing files, or remembering things for you. This guide explains everything step-by-step, so you’ll feel right at home, and it’s written to help OmniMind shine on GitHub—maybe even as "repo of the day" or "week"!

---

## Why OmniMind is Great for You

OmniMind is all about making MCP and AI easy and helpful. Here’s what you’ll enjoy:
- **Quick to Start**: Get going with just a few steps—perfect for anyone, even if you’re new.
- **Built-In Helpers**: Comes with tools like Fetch (web stuff), Memory (saving info), and Filesystem (file tasks)—ready to use right away.
- **Smart Answers**: Uses Google Gemini to give you fast, clear responses every time.
- **Free for All**: No cost, and you can change it however you like—it’s open-source!
- **Fits Your Needs**: Add your own MCP servers to do exactly what you want.
- **Friendly for Everyone**: Simple enough for beginners, powerful enough for pros.

---

## Before You Begin

To use OmniMind, you need two things set up. Don’t worry—it’s easier than it sounds!

1. **Google Gemini API Key**: This powers the AI part of OmniMind. Here’s how to get it:
   - Go to the Google Cloud website, sign up, and grab your API key (it’s like a password for the AI).
   - Save it on your computer as an environment variable called `GOOGLE_API_KEY`:
     - **Windows**: Open Command Prompt and type `set GOOGLE_API_KEY=your-api-key-here`.
     - **Mac/Linux**: Open Terminal and type `export GOOGLE_API_KEY=your-api-key-here`.
   - This lets OmniMind talk to Google Gemini for smart, fast answers!
2. **Config File**: OmniMind needs a file to know which MCP servers to connect to. We’ll show you how to make one—it’s your list of helpers!

---

## Basic Usage: Chat with OmniMind

Let’s start with the easiest way to use OmniMind—chatting! You’ll need a config file, even for this, because it tells OmniMind which helpers to use.

### Step 1: Install OmniMind
Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:
```bash
pip install omnimind
```

### Step 2: Make a Config File
Create a file called `my_config.json` and add this:
```json
{
    "mcpServers": {
        "fetch": {
            "command": "uvx",
            "args": ["mcp-server-fetch"]
        },
        "memory": {
            "command": "C:\\Program Files\\nodejs\\npx.cmd",
            "args": ["-y", "@modelcontextprotocol/server-memory"],
            "env": {
                "MEMORY_FILE_PATH": "C:\\path\\to\\your\\memory.json"
            }
        },
        "filesystem": {
            "command": "C:\\Program Files\\nodejs\\npx.cmd",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\path\\to\\source", "C:\\path\\to\\workspace"]
        }
    }
}
```
- **What’s Happening**: This sets up three helpers—Fetch for web stuff, Memory for saving things, and Filesystem for file tasks.
- **Fix the Paths**: Change `C:\\path\\to\\your\\memory.json` and other paths to real folders on your computer (e.g., `C:\\Users\\YourName\\Desktop\\memory.json`). Use `/` instead of `\` on Mac/Linux.
- **Why It’s Great**: These helpers are ready to go, and you can add more later!

### Step 3: Run a Chat
Create a Python file (like `chat.py`) and add this:
```python
from omnimind import OmniMind

agent = OmniMind(config_path="my_config.json")
agent.run()
```

### Step 4: Start Chatting
Run it with `python chat.py`. You’ll see “Ready! Type 'quit' to exit.” Type something like “What’s my favorite color?” or “List files in my directory”—it’ll answer using the servers in your config! Type `quit` to stop.

**Why It’s Great**: You’re talking to AI in minutes, it’s free, and it works with MCP helpers right away—no hard setup needed.

---

## Advanced Usage: Do More with MCP Servers

Want to use OmniMind for bigger tasks? You can fetch web info, save it, and work with files—all with the same config file from above.

### Step 1: Use Your Config
Stick with `my_config.json` from the chat section—it’s got Fetch, Memory, and Filesystem ready.

### Step 2: Write a Script
Create a file (like `multi_task.py`) and add this:
```python
from omnimind import OmniMind
import os

# Check your API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Please set the GOOGLE_API_KEY environment variable!")
    exit()

# Start OmniMind
agent = OmniMind(config_path="my_config.json", api_key=api_key)

# Run it
agent.run()
```

### Step 3: Try Some Tasks
Run it with `python multi_task.py`. Type these one by one:
- “Summarize https://example.com”  
  - Fetch grabs the webpage and gives you a short version—perfect for quick info!
- “Remember my favorite color is blue”  
  - Memory saves it for later—great for keeping track of things!
- “Create a file named example.txt”  
  - Filesystem makes the file—handy for saving stuff!

**Why It’s Great**: You can do lots of tasks with one tool, it’s fast, and it’s all free and easy to use.

### Example Prompts to Try
Here are some things you can say with the Fetch, Memory, and Filesystem servers:
- **File Operations**:  
  - “Create a file named example.txt”  
  - “Search for ‘function’ in all Python files”  
  - “Count lines in main.py”  
- **Web Content**:  
  - “Summarize https://example.com”  
  - “Extract headlines from news site”  
- **System Commands**:  
  - “List files in current directory”  
  - “Check Python version”  
  - “Run git status”  
- **Memory Operations**:  
  - “Remember my favorite color is blue”  
  - “What preferences did I set?”  
  - “Show recent commands”  

**Why It’s Great**: These examples show how flexible OmniMind is, and they work right away with your config!

---

## Adding Your Own MCP Servers

Want to do even more? Add your own MCP servers to OmniMind—it’s simple and lets you customize everything.

### Option 1: Update Your Config File
Add a new server to `my_config.json`:
```json
{
    "mcpServers": {
        "my_server": {
            "command": "python",
            "args": ["my_server.py"]
        }
    }
}
```
- Replace `my_server.py` with your own script—check the [MCP official docs](https://github.com/modelcontextprotocol) for how to make one.
- Next time you run OmniMind, it’ll use your server too!

### Option 2: Add It in Code
Or, add it right in your script:
```python
from omnimind import OmniMind

agent = OmniMind(config_path="my_config.json")
agent.add_server("my_server", command="python", args=["my_server.py"])
agent.run()
```

### Finding More Servers
Need ideas? Check out [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers/)—it’s a big list of MCP servers you can add. Each one might need different prompts, so tweak what you say to match the server.

**Why It’s Great**: You can make OmniMind do exactly what you need, it’s free to play with, and there’s a whole world of servers to try!

---

## Tips to Get the Most Out of OmniMind

- **Look at Examples**: The [examples/](examples/) folder has scripts to copy—like chats or multi-server tasks.
- **Explore Servers**: Visit [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers/) for more helpers to add.
- **Read More**: Check [installation.md](installation.md) for setup help or [api_reference.md](api_reference.md) for all the details.
- **Ask Us**: Stuck? Post in [discussions](https://github.com/Techiral/OmniMind/discussions)—we’re happy to help!

**Why It’s Great**: You’ve got tons of support, it’s easy to learn more, and you’ll never feel lost.

---

## Why OmniMind Could Be Repo of the Day or Week

OmniMind is special—it’s your entry point to MCP and AI in Python. Here’s why it’s getting attention:
- **Big Trends**: MCP and AI are hot topics, and OmniMind makes them simple for everyone.
- **Easy for All**: Beginners love how quick it is, pros love how much it can do.
- **Community Fun**: It’s open-source, so anyone can join and make it better.
- **Always Improving**: New updates and servers keep it exciting.

Help it grow—star it on [GitHub](https://github.com/Techiral/OmniMind/) and share it with #OmniMindAI!

---

## Ready to Jump In?

OmniMind is your way to explore MCP and AI—free, simple, and full of possibilities. Chat with it, fetch web info, save memories, manage files—it’s all here. Try it, add your own servers, and join the fun—let’s make MCP easy for everyone together!

Questions? Email [techiralthefuture@gmail.com](mailto:techiralthefuture@gmail.com) or visit [https://github.com/Techiral/OmniMind/](https://github.com/Techiral/OmniMind/).