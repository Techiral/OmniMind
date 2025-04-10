import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="omnimind",
    version="0.1.1",
    author="Lakshya Gupta",
    author_email="techiralthefuture@gmail.com",
    description="A plug-and-play Python library for effortless MCP server integration, powered by Google Gemini",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Techiral/OmniMind",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='open-source, MCP, Model-Context-Protocol, OmniMind, MCP Server, MCP Client, python, AI Agents, AI workflows, AI Automations, AI Tools, Plug & Play, Techiral, Google Gemini',
    python_requires='>=3.6',
)
