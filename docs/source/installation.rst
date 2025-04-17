.. _installation:

Installation
============

Welcome to OmniMind! This Python library makes MCP (Model Context Protocol) and AI easy and fun for everyone. Whether you’re a coder, a complete beginner, a solopreneur, or a business owner, installing OmniMind is simple and quick—no tricky steps here! This guide walks you through everything you need to get started, and we’ve added ways for you to help make OmniMind a top project on GitHub—maybe even "repo of the day"!

Why Installing OmniMind is Easy
-------------------------------

OmniMind is built to get you going fast. Here’s what makes it great:

- **Simple Steps**: Just a few things to do, and you’re ready—no hard stuff to figure out.
- **Works on Any Computer**: Windows, Mac, or Linux—it’s all good.
- **Free to Use**: No cost, and it’s open-source, so you can try it risk-free.
- **Quick Setup**: Takes just minutes, even if you’ve never coded before.
- **Helpful Tools Included**: Comes with MCP servers like Fetch, Memory, and Filesystem—ready to go!

Let’s get started—it’s easier than you think!

What You’ll Need
----------------

Before we begin, you need two things. Don’t worry—we’ll make it simple!

1. **Python**: This is what runs OmniMind. Most computers have it, but we’ll check.
2. **A Terminal**: A place to type commands—like Command Prompt (Windows) or Terminal (Mac/Linux). It’s already on your computer!

Step 1: Check or Install Python
------------------------------

OmniMind needs Python to work, and it’s super easy to get.

For Non-Technical Users
~~~~~~~~~~~~~~~~~~~~~~

- **Windows**: Press ``Windows Key + R``, type ``cmd``, and hit Enter. In the black box, type ``python --version``. If you see something like “Python 3.8.0,” you’re set! If not, download it from `python.org <https://www.python.org/downloads/>`_. Click the big “Download Python” button, run the file, and check “Add Python to PATH” during setup.
- **Mac**: Open Terminal (search “Terminal” in Spotlight), type ``python3 --version``, and press Enter. If it shows a version, you’re good! If not, it’ll ask to install it—say yes and follow along.
- **Linux**: Open Terminal, type ``python3 --version``, and hit Enter. If it’s there, great! If not, type ``sudo apt install python3`` (Ubuntu) or ask a friend to help.

**Why It’s Great**: Python is free, quick to install, and OmniMind works with any version 3.8 or higher—super flexible!

Step 2: Install OmniMind
------------------------

Now that Python’s ready, let’s add OmniMind!

1. **Open Your Terminal**:

   - Windows: Press ``Windows Key + R``, type ``cmd``, and hit Enter.
   - Mac/Linux: Search “Terminal” and open it.

2. **Type This Command**:

   .. code-block:: bash

      pip install omnimind

   Press Enter, and it’ll download OmniMind in seconds. If it says “pip is not recognized,” try:

   .. code-block:: bash

      python -m pip install omnimind

3. **Check It Worked**:

   .. code-block:: bash

      python -c "import omnimind; print('OmniMind is ready!')"

   If you see “OmniMind is ready!”—you’re done!

**Why It’s Great**: One command gets you everything—no complicated downloads or setups. It’s fast and works every time!

Step 3: Set Up Your Google Gemini API Key
----------------------------------------

OmniMind uses Google Gemini for smart AI answers, and it needs a key to connect. Here’s how to do it—super simple!

1. **Get Your Key**:

   Go to `Google Cloud Console <https://console.cloud.google.com/>`_, sign in (or sign up—it’s free to start), and create a project (call it “OmniMind” if you like!). Search for “Gemini API,” enable it, and click “Create Credentials” to get an API key. Copy it—it’s a string like ``your-api-key-here``.

2. **Save It on Your Computer**:

   - **Windows**: In Command Prompt, type:

     .. code-block:: bash

        set GOOGLE_API_KEY=your-api-key-here

     and press Enter.
   - **Mac/Linux**: In Terminal, type:

     .. code-block:: bash

        export GOOGLE_API_KEY=your-api-key-here

     and press Enter.

     This only lasts until you close the window—see “Make It Permanent” below if you want it to stick.

3. **Make It Permanent (Optional)**:

   - **Windows**: Search “Environment Variables” in the Start menu, click “Edit environment variables for your account,” add a new variable named ``GOOGLE_API_KEY``, and paste your key.
   - **Mac/Linux**: Open Terminal, type:

     .. code-block:: bash

        echo "export GOOGLE_API_KEY=your-api-key-here" >> ~/.bashrc

     (or ``~/.zshrc`` for Mac), and restart Terminal.

**Why It’s Great**: This key connects OmniMind to Google Gemini for fast, smart answers—it’s free to try, and setup takes just a minute!

Step 4: Add a Config File
-------------------------

OmniMind needs a list of MCP servers (helpers) to work with. Let’s make one—it’s easy!

1. **Create a File**:

   Open Notepad (Windows) or TextEdit (Mac), or any text editor. Paste this:

   .. code-block:: json

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

   Change ``YourName`` to your actual username (e.g., ``C:\\Users\\John\\Desktop``). Use ``/`` instead of ``\`` on Mac/Linux (e.g., ``/home/john/Desktop``). Save it as ``my_config.json`` on your Desktop.

2. **Why These Servers?**:

   - ``fetch``: Grabs web info—like summaries of pages.
   - ``memory``: Saves things—like your favorite color.
   - ``filesystem``: Works with files—like creating or listing them.

3. **Need Node.js?**:

   The ``memory`` and ``filesystem`` servers use Node.js. If they don’t work, download it from `nodejs.org <https://nodejs.org/>`_—click the big green button, install it, and you’re set!

**Why It’s Great**: This file gets you started with useful helpers right away, and it’s simple to copy and paste—no coding needed yet!

Step 5: Try It Out
------------------

You’re ready! Let’s test OmniMind with a quick chat.

1. **Make a File**:

   Open Notepad or TextEdit, paste this:

   .. code-block:: python

      from omnimind import OmniMind

      agent = OmniMind(config_path="C:\\Users\\YourName\\Desktop\\my_config.json")
      agent.run()

   Fix the path to match where you saved ``my_config.json`` (e.g., ``/home/john/Desktop/my_config.json`` on Mac/Linux). Save it as ``test.py`` on your Desktop.

2. **Run It**:

   Open your terminal, type:

   .. code-block:: bash

      cd Desktop
      python test.py

   and press Enter. You’ll see “Ready! Type 'quit' to exit.” Type “What’s on example.com?” or “List files in my directory”—it’ll answer!

3. **Have Fun**:

   Try more—check :ref:`quickstart` for ideas like saving memories or fetching web summaries.

**Why It’s Great**: You’re using MCP and AI in minutes, it’s free, and it works for everyone—no experience required!

Help Make OmniMind Even Better
------------------------------

Love OmniMind? Here’s how you can help it grow and maybe get it trending on GitHub:

- **Star It**: Click the ⭐ button at `GitHub <https://github.com/Techiral/OmniMind/>`_—it helps others find us!
- **Share It**: Tell friends on X with #OmniMindAI or in groups—it’s a cool way to spread the word.
- **Join In**: Have an idea? Post in `GitHub Discussions <https://github.com/Techiral/OmniMind/discussions>`_ or add your own servers—see :ref:`tutorials/custom_server`.
- **Say Hi**: Email `techiralthefuture@gmail.com <mailto:techiralthefuture@gmail.com>`_ with feedback—we’d love to hear from you!

**Why It’s Great**: Your support makes OmniMind a go-to tool for MCP and AI, and it’s fun to be part of something big!

Extra Tips
----------

- **Stuck?**: Check :ref:`faq` or ask in `GitHub Discussions <https://github.com/Techiral/OmniMind/discussions>`_—we’re here to help.
- **More Servers?**: Find tons of MCP servers at `Awesome MCP Servers <https://github.com/punkpeye/awesome-mcp-servers/>`_ to add to your config.
- **Keep It Simple**: Start with the basics—you can grow from there as you get comfy!

**Why It’s Great**: You’ve got all the help you need, it’s free to explore, and it’s made for everyone—no barriers here!

Ready to Go?
------------

That’s it—OmniMind is installed and ready! It’s your easy way into MCP and AI with Python—fast, free, and fun. Try it out, share it, and help make it a top repo. Let’s make MCP simple for everyone together!