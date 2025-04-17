.. _tutorials/custom_server:

Building a Custom MCP Server
===========================

OmniMind’s strength lies in its flexibility to integrate custom MCP servers. This tutorial shows how to create a server that fetches data from an API.

Prerequisites
-------------

- OmniMind installed (:ref:`installation`).
- Basic Python knowledge.

Step 1: Write the Server Script
------------------------------

Create `api_server.py`:

.. code-block:: python

   import requests
   import sys

   query = sys.argv[1] if len(sys.argv) > 1 else "default"
   response = requests.get(f"https://api.example.com/data?q={query}")
   print(response.json())

Step 2: Connect to OmniMind
--------------------------

Use OmniMind to run the server:

.. code-block:: python

   from omnimind import Agent

   agent = Agent()
   agent.add_server("api_server", command="python", args=["api_server.py"])
   result = agent.run("search_term")
   print(result)

This sends "search_term" to your server and prints the API response.

Step 3: Scale Up
---------------

Add multiple servers or integrate with Google Gemini. See :ref:`tutorials/gemini_integration`.

Share your server on `GitHub <https://github.com/Techiral/OmniMind>`_!