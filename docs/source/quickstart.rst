.. _quickstart:

Quickstart
==========

Welcome to OmniMind! This Python library makes it easy and fun to work with MCP (Model Context Protocol) and AI. Whether you’re a beginner who’s never coded, a developer building projects, a solopreneur saving time, or a business owner adding smart tools, this guide gets you started in minutes. OmniMind connects you to MCP servers—helpers that fetch web info, manage files, or remember things—powered by Google Gemini for smart answers. Let’s dive in and make OmniMind shine on GitHub—maybe even as "repo of the day"!

Step 1: Install OmniMind
-----------------------

Before you begin, ensure you have OmniMind installed and a Google Gemini API key set up. See :ref:`installation` for detailed instructions on installing OmniMind, setting the ``GOOGLE_API_KEY`` environment variable, and creating a config file (``my_config.json``) with default MCP servers (Fetch, Memory, Filesystem).

Step 2: Chat with OmniMind
--------------------------

Let’s start with the easiest way to use OmniMind—chatting with AI and MCP servers!

1. **Use Your Config File**:

   Ensure you have a ``my_config.json`` file from :ref:`installation`. It should look like this:

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

   Replace ``YourName`` with your actual username (e.g., ``C:\\Users\\John\\Desktop``). On Mac/Linux, use ``/`` (e.g., ``/home/john/Desktop``).

   **What’s Happening**: This sets up Fetch (web info), Memory (saving data), and Filesystem (file tasks) servers.

2. **Create a Chat Script**:

   Create a file named ``chat.py`` and add:

   .. code-block:: python

      from omnimind import OmniMind

      agent = OmniMind(config_path="C:\\Users\\YourName\\Desktop\\my_config.json")
      agent.run()

   Update the path to match where you saved ``my_config.json`` (e.g., ``/home/john/Desktop/my_config.json`` on Mac/Linux).

3. **Run and Chat**:

   Open your terminal, navigate to the folder with ``chat.py`` (e.g., ``cd Desktop``), and run:

   .. code-block:: bash

      python chat.py

   You’ll see “Ready! Type 'quit' to exit.” Try typing:
   - “What’s on example.com?” (Fetch summarizes the webpage)
   - “Remember my favorite color is blue” (Memory saves it)
   - “List files in my directory” (Filesystem lists files)

   Type ``quit`` to stop.

**Why It’s Great**: You’re chatting with AI and MCP servers in minutes, it’s free, and it works for everyone—no coding experience needed!

Step 3: Do More with MCP Servers
-------------------------------

Want to use OmniMind for bigger tasks? Try fetching web info, saving data, or managing files with the same config.

1. **Create a Multi-Task Script**:

   Create a file named ``multi_task.py`` and add:

   .. code-block:: python

      from omnimind import OmniMind
      import os

      # Check API key
      api_key = os.getenv("GOOGLE_API_KEY")
      if not api_key:
          print("Please set the GOOGLE_API_KEY environment variable!")
          exit()

      # Start OmniMind
      agent = OmniMind(config_path="C:\\Users\\YourName\\Desktop\\my_config.json", api_key=api_key)
      agent.run()

   Update the config path as before.

2. **Run and Try Tasks**:

   Run with:

   .. code-block:: bash

      python multi_task.py

   Type these prompts one by one:
   - “Summarize https://example.com” (Fetch gives a webpage summary)
   - “Remember my favorite color is blue” (Memory saves it)
   - “Create a file named example.txt” (Filesystem creates the file)

   Try more prompts like:
   - “Search for ‘function’ in all Python files” (Filesystem)
   - “Check Python version” (System command)
   - “What preferences did I set?” (Memory)

**Why It’s Great**: You can handle web, memory, and file tasks with one tool, it’s fast, and it’s all free and flexible.

Step 4: Explore More
--------------------

- **Add Your Own Servers**: Customize OmniMind with new MCP servers. See :ref:`tutorials/custom_server` for how to add a server via code or config.
- **Try Google Gemini Features**: Enhance AI capabilities with Gemini. Check :ref:`tutorials/gemini_integration`.
- **Discover More Servers**: Find additional MCP servers at `Awesome MCP Servers <https://github.com/punkpeye/awesome-mcp-servers/>`_.
- **Join the Community**: Share your setup or ask questions in `GitHub Discussions <https://github.com/Techiral/OmniMind/discussions>`_ or email `techiralthefuture@gmail.com <mailto:techiralthefuture@gmail.com>`_. Star us on `GitHub <https://github.com/Techiral/OmniMind/>`_ and support our Product Hunt launch on April 19, 2025!

**Why It’s Great**: OmniMind grows with you, it’s free to explore, and our community is here to help make it a top repo!