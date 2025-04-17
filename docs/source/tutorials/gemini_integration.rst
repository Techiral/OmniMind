.. _tutorials/gemini_integration:

Google Gemini Integration
=========================

OmniMind seamlessly integrates with Google Gemini for advanced AI capabilities. This tutorial shows how to set it up.

Prerequisites
-------------

- OmniMind and `google-generativeai` installed (:ref:`installation`).
- Google Gemini API key.

Step 1: Configure Gemini
-----------------------

Set your API key:

.. code-block:: python

   import os
   os.environ["GEMINI_API_KEY"] = "your_api_key"

Step 2: Run OmniMind with Gemini
-------------------------------

Connect a server and use Gemini:

.. code-block:: python

   from omnimind import Agent

   agent = Agent()
   agent.add_server("my_server", command="python", args=["my_server.py"])
   agent.enable_gemini()
   response = agent.run("What is MCP?")
   print(response)

This queries Gemini through your MCP server.

Step 3: Explore More
--------------------

Try custom prompts or multiple servers. Share your setup in our `GitHub Discussions <https://github.com/Techiral/OmniMind/discussions>`_!