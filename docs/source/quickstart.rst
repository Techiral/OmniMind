.. _quickstart:

Quickstart
==========

This guide shows how to set up OmniMind and add a custom MCP server in minutes.

Step 1: Install OmniMind
-----------------------

See :ref:`installation` for setup instructions.

Step 2: Create a Custom MCP Server
---------------------------------

Create a simple server script (e.g., `my_server.py`):

.. code-block:: python

   # my_server.py
   print("Hello from my custom MCP server!")

Step 3: Integrate with OmniMind
------------------------------

Run the following code to connect your server:

.. code-block:: python

   from omnimind import Agent

   agent = Agent()
   agent.add_server("my_server", command="python", args=["my_server.py"])
   agent.run()

This connects your server to OmniMind’s AI pipeline.

Step 4: Explore More
--------------------

Try integrating Google Gemini or building complex servers. See :ref:`tutorials/custom_server` for advanced examples.

Join our `GitHub Discussions <https://github.com/Techiral/OmniMinddiscussions>`_ to share your setup!