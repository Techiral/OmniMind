# Configuring OmniMind

Hey there! Welcome to configuring OmniMind—the Python library that makes MCP (Model Context Protocol) and AI simple and fun for everyone. Whether you’re new to coding, a developer building cool stuff, a solopreneur saving time, or a business owner adding smart features, this guide has everything you need to set up OmniMind your way. It’s free, open-source, and easy to tweak—perfect for all skill levels! Plus, your help can make OmniMind a trending hit on GitHub with keywords like MCP, AI, and Python library driving it up the ranks.

---

## Why Configuring OmniMind is Easy and Awesome

OmniMind uses a config file to connect to MCP servers—think of them as helpers that do tasks like fetching web info, managing files, or saving details. Here’s why setting it up is great:
- **Simple to Start**: Just copy and paste—no hard steps, even if you’ve never coded.
- **Ready-Made Helpers**: Comes with tools like Fetch, Memory, and Filesystem—free and ready to use.
- **Change It Anytime**: Add your own servers or adjust it to fit your needs—it’s flexible.
- **Free and Open**: No cost, and you can share or tweak it because it’s open-source.
- **Honest Approach**: It’s not perfect yet (sometimes errors pop up), but we’ve got fixes and a community to help!

Let’s get your OmniMind config ready—it’s quick and fun!

---

## What You’ll Need

Before we dive in, you need OmniMind installed—check [installation.md](installation.md) for the easy steps. You’ll also need a text editor (like Notepad on Windows or TextEdit on Mac) to make your config file. That’s it—no fancy tools required!

---

## Step 1: Understanding the Config File

OmniMind needs a file (like `my_config.json`) to know which MCP servers to connect to. It’s a simple list in JSON format—don’t worry if that sounds new; it’s just text you can copy and change. Here’s a basic one to start with:

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
                "MEMORY_FILE_PATH": "C:\\Users\\YourName\\Desktop\\memory.json"
            }
        },
        "filesystem": {
            "command": "C:\\Program Files\\nodejs\\npx.cmd",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\Users\\YourName\\Desktop", "C:\\Users\\YourName\\Desktop\\workspace"]
        }
    }
}
```

### What This Does
- **fetch**: Grabs stuff from the web—like page summaries.
- **memory**: Saves info—like your favorite color.
- **filesystem**: Works with files—like listing or creating them.

**Why It’s Great**: These helpers come free with OmniMind, and they’re ready to go with Google Gemini powering the AI—simple and smart!

---

## Step 2: Making Your Config File

Let’s set it up—it’s as easy as copying and pasting!

1. **Open a Text Editor**:
   - Windows: Search “Notepad” and open it.
   - Mac: Search “TextEdit” and open it (set it to plain text in Format > Make Plain Text).
   - Linux: Use any editor like `nano` in Terminal.
2. **Copy the Example**:
   - Paste the config above into your editor.
3. **Fix the Paths**:
   - Change `YourName` to your actual username (e.g., `C:\\Users\\John\\Desktop`).
   - Make sure the folders exist—create `memory.json` and a `workspace` folder on your Desktop if they’re not there.
   - On Mac/Linux, use `/` instead (e.g., `/home/john/Desktop/memory.json`).
4. **Save It**:
   - Save as `my_config.json` on your Desktop—call it whatever you want, just remember where it is!

**Why It’s Great**: Takes a minute, no coding needed, and you’re ready to use MCP and AI with OmniMind!

---

## Step 3: Using Your Config

Now, let’s connect OmniMind to your helpers!

1. **Run a Simple Chat**:
   - Make a file (e.g., `test.py`) and add:
     ```python
     from omnimind import OmniMind

     agent = OmniMind(config_path="C:\\Users\\YourName\\Desktop\\my_config.json")
     agent.run()
     ```
   - Fix the path to match where you saved your file (e.g., `/home/john/Desktop/my_config.json`).
   - Run it with `python test.py` in your terminal—type “Summarize https://example.com” and see it work!
2. **Try More**:
   - Check [usage.md](usage.md) for fun tasks like saving memories or listing files.

**Why It’s Great**: It’s quick to start, free to try, and works for everyone—no skills required!

---

## Adding Your Own MCP Servers

Want more helpers? You can add any MCP server you like—it’s simple and open-source!

### Option 1: Edit Your Config
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
- Replace `my_server.py` with your script—find ideas at [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers/).
- Save and run OmniMind—it’ll use your new server!

### Option 2: Add in Code
Or, do it in your script:
```python
from omnimind import OmniMind

agent = OmniMind(config_path="my_config.json")
agent.add_server("my_server", command="python", args=["my_server.py"])
agent.run()
```

**Why It’s Great**: You’re in charge—add whatever you need, and it’s free and easy to do!

### Where to Find More Servers
Check [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers/)—a big, free list of MCP servers. Copy their setup into your config, and you’re set! Not sure how? Ask us in [discussions](https://github.com/Techiral/OmniMind/discussions)—we’re here to help.

**Why It’s Great**: Tons of options, all free, and you can grow OmniMind your way!

---

## Fixing Common Setup Questions

### What If My Paths Are Wrong?
If OmniMind says it can’t find a file:
- Double-check your paths in `my_config.json` (e.g., `C:\\Users\\YourName\\Desktop`).
- Make sure those folders exist—create them if not.
- Try again—it’ll work once the paths match!

**Why It’s Great**: Easy fix, and you’re back on track fast!

### Do I Need Node.js?
Yes, for servers like `memory` and `filesystem` in the example. If they don’t work, grab Node.js from [nodejs.org](https://nodejs.org/)—click the green button, install it, and you’re good. Not all servers need it, so start with `fetch` if you want to skip this!

**Why It’s Great**: Free and quick to add, and it unlocks more helpers!

### What If I Get an Error?
OmniMind isn’t perfect yet—sometimes errors happen (like a server not starting). Check your paths, API key (in [installation.md](installation.md)), and try again. Still stuck? Share it in [discussions](https://github.com/Techiral/OmniMind/discussions)—we’ll fix it together!

**Why It’s Great**: Errors are no big deal—we’re honest about it, and help is always here!

---

## Branding and Open-Source Fun

OmniMind is more than a tool—it’s a community project! Here’s how we roll:
- **Honest Team**: We’re Techiral, making MCP and AI simple. It’s not flawless yet, but we’re improving every day—your feedback helps!
- **Open-Source Love**: Free for all, and you can add to it—check [CONTRIBUTING.md](CONTRIBUTING.md).
- **Join the Party**: Star us at [https://github.com/Techiral/OmniMind/](https://github.com/Techiral/OmniMind/), share with #OmniMindAI, or chat in [discussions](https://github.com/Techiral/OmniMind/discussions)—let’s make it big!

**Why It’s Great**: You’re part of something growing, free, and fun—help us rank higher with every click!

---

## Extra Tips

- **Start Small**: Use the example config—add more as you go.
- **Need Ideas?**: See [usage.md](usage.md) for what your servers can do.
- **Questions?**: Email [techiralthefuture@gmail.com](mailto:techiralthefuture@gmail.com)—we reply fast!

**Why It’s Great**: Everything’s here to make it easy, free, and exciting for you!

---

## Make OmniMind Yours

Configuring OmniMind is your ticket to MCP and AI in Python—simple, free, and open-source. Copy the config, tweak it, add your servers—it’s all up to you. Help us make it a top repo—star it, share it, and let’s bring MCP to everyone together!