# docs/source/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'OmniMind'
copyright = '2025, Techiral'
author = 'Lakshya Gupta'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

html_meta = {
    'description': 'OmniMind is an open‑source Python library that seamlessly integrates the Model Context Protocol (MCP) with AI agents, workflows, and automations, providing plug‑and‑play tools for both servers and clients and full compatibility with Google Gemini.',
    'keywords': 'OmniMind, MCP, Model Context Protocol, Python, AI, open-source, model context protocol, what is model context protocol, claude model context protocol, model context protocol claude, anthropic model context protocol, model context protocol anthropic, model context protocol explained, open source protocol, protocol, mcp protocol, communication protocol, ai protocols, model integration, ai data access protocol, ai context modeling, context, local file context, deep learning protocols, mcp open source protocol, large language models, mcp, claude mcp, ai mcp, mcp tutorial, mcp agents, mcp server, cursor mcp, mcp servers, mcp tools, mcp explained, mcp n8n, mcp llms, mcp guide, mcp ai, mcp client, what is mcp, mcp python, no code mcp, mcp clients, mcp ai agents, mcp templates, mcp pydantic ai, mcp agent, github mcp, mcp vs code, mcp database, how to use mcp, windsurf mcp, mcp tutorials, mcp anthropic, mcp llm, mcp sdk, mcp host, mem0 mcp, agno mcp, mcp crash course, github mcp server, ai agents, ai agent, claude mcp agents, n8n mcp agent, ai agent startup, anthropic mcp, mcp setup, agentic research mcp server, claude agents, ai agents 2025, build ai agents',
}