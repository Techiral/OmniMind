from setuptools import setup, find_packages

setup(
    name="omnimind",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mcp",
        "langchain-google-genai",
        "langgraph",
        "langchain-mcp-adapters",
        "python-dotenv"
    ],
    author="Techiral",
    author_email="techiralthefuture@gmail.com",
    description="A plug-and-play MCP client library for AI tool integration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Techiral/OmniMind",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)