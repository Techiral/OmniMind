# OmniMind

Welcome to OmniMind—an **open-source** Python library designed for effortless **MCP (Model Context Protocol)** integration. It simplifies working with **AI Agents**, **AI workflows**, and **AI Automations**, making it accessible to developers building **AI Tools**, beginners exploring **MCP Servers** and **MCP Clients**, and businesses seeking to enhance their projects. OmniMind is designed as a **Plug & Play** solution, is free to use, and provides all the necessary components to get started with **python** and **AI** development. Created by **Techiral**, OmniMind is your gateway to streamlined **AI** development. Join **Techiral** and the OmniMind team in building the future of AI!

[![GitHub Stars](https://img.shields.io/github/stars/Techiral/OmniMind?style=social)](https://github.com/Techiral/OmniMind/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Techiral/OmniMind?style=social)](https://github.com/Techiral/OmniMind/network)
[![Build Status](https://github.com/Techiral/OmniMind/actions/workflows/welcome.yml/badge.svg)](https://github.com/Techiral/OmniMind/actions)
[![License](https://img.shields.io/github/license/Techiral/OmniMind)](https://github.com/Techiral/OmniMind/blob/main/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/omnimind)](https://pypistats.org/packages/omnimind)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-techiral-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/techiral/)
[![YouTube](https://img.shields.io/badge/YouTube-@techiral-red?style=flat-square&logo=youtube)](https://www.youtube.com/@techiral)

---

<p align="center">
  <img src="demo\OmniMind.png" width="1536" height="1024">
</p>

## What’s OmniMind All About?

OmniMind is an **open-source** **python** library designed to simplify **Model Context Protocol (MCP)** integration for **AI Agents**, **AI workflows**, and **AI Automations**. It provides a **Plug & Play** experience for connecting to **MCP Servers** and utilizing various **AI Tools**. Whether you're a seasoned developer or just starting with **AI**, OmniMind offers a streamlined approach to building intelligent applications. Here's why you'll love using OmniMind:

- **Easy to Start**: You can get going with just one line of code—no complicated setup needed.
- **Works Right Away**: Comes with tools like Terminal, Fetch, Memory, and Filesystem, ready to use out of the box.
- **Smart Answers**: Uses Google Gemini to give you fast, reliable responses every time.
- **Free for Everyone**: Open-source means you can use it, change it, and share it without spending a dime.
- **Fits Your Needs**: Add your own MCP servers or tweak it however you want—it’s flexible.
- **Helpful Community**: Join others who are using OmniMind and get support when you need it.

It’s perfect for developers coding AI apps, beginners learning MCP, solopreneurs automating tasks, or entrepreneurs building new ideas.

---

## How to Get Started

Getting OmniMind up and running takes just a few minutes. Here’s how:

### 1. Install It
Run this command in your terminal:
```bash
pip install omnimind
```

### 2. Try It Out
Open a Python file and type this:
```python
from omnimind import OmniMind

agent = OmniMind()
agent.run()  # Start asking questions like "What’s in my files?" or "Hi there!"
```

That’s it! You’re now connected to MCP servers and chatting with AI. Want to see more? Check out the [examples/](examples/) folder for ideas.

---

## Why You’ll Like Using OmniMind

- **Saves Time**: Connects to MCP servers fast, so you can focus on what you’re building.
- **Lots of Tools**: Comes with everything from file access to web fetching, all set up for you.
- **Smart and Fast**: Google Gemini makes sure you get good answers quickly.
- **No Cost**: Free to use and share, making it great for any budget.
- **Easy to Change**: Add your own servers or adjust it to fit your project perfectly.
- **Works for Everyone**: Whether you’re new to coding or a pro, it’s simple to pick up.
- **Keeps Getting Better**: Regular updates mean more features and fixes based on what users say.

---

## What’s Inside the Repo?

Here’s what you’ll find in this repository:
- **[docs/](docs/)**: Guides for installing, using, and learning more about OmniMind.
- **[examples/](examples/)**: Ready-to-run scripts to show you what it can do.
- **[omnimind/](omnimind/)**: The main code that makes OmniMind work.
- **[tests/](tests/)**: Checks to make sure everything runs smoothly.
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: How you can help make OmniMind even better.
- **[SECURITY.md](SECURITY.md)**: Info on keeping things safe and reporting issues.

Take a look around—it’s all here to help you get the most out of OmniMind!

---

## How to Make It Your Own

Want to add your own MCP server? It’s easy:
```python
agent = OmniMind()
agent.add_server("my_server", command="python", args=["my_server.py"])
agent.run()  # Your server’s now part of the mix!
```

Check out [configuration.md](docs/configuration.md) for more details on customizing OmniMind.

---

## Join the Community

We’d love for you to be part of OmniMind! Here’s how:
- **Star the Repo**: Click the ⭐ button at the top to show your support—it helps others find us!
- **Share Your Thoughts**: Open an [issue](https://github.com/Techiral/OmniMind/issues) or join [discussions](https://github.com/Techiral/OmniMind/discussions).
- **Help Out**: Add features or fix bugs—see [CONTRIBUTING.md](CONTRIBUTING.md) for how to get started.
- **Tell Others**: Post about OmniMind on X or anywhere you hang out online with #OmniMindAI.

Your ideas and feedback make OmniMind better for everyone!

---

## See It in Action

Here’s a quick peek at OmniMind working its magic:

<video src="demo/OmniMind.mp4" width="600" controls muted loop>
  Your browser does not support the video tag.
</video>

---

## License

OmniMind is free to use under the [MIT License](LICENSE). That means you can do whatever you want with it—use it, change it, share it—all at no cost.

---

## Why Contribute to OmniMind?

Contributing to OmniMind offers a unique opportunity to:

*   **Learn and Grow:** Expand your knowledge of MCP, AI Agents, and cutting-edge technologies.
*   **Build a Portfolio:** Showcase your skills and contributions to a growing open-source project.
*   **Collaborate with Experts:** Work alongside experienced developers and AI enthusiasts.
*   **Make a Difference:** Help shape the future of AI development and empower others to build intelligent applications.

## Contributing

We welcome contributions to OmniMind! If you're passionate about **open-source**, **AI Agents**, **AI workflows**, or **Model Context Protocol (MCP)**, we encourage you to contribute to OmniMind. Check out our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines and instructions on how to get started. Let's build the future of AI together!

## Code of Conduct

Please note that OmniMind has a Code of Conduct. By participating in this project, you agree to abide by its terms.

## Questions?

Got a question or idea? Reach out:
- Email: [techiralthefuture@gmail.com](mailto:techiralthefuture@gmail.com)  
- GitHub: [https://github.com/Techiral/OmniMind/](https://github.com/Techiral/OmniMind/)  
- X: Follow us at [@techiral_](https://x.com/techiral_)

Thanks for checking out OmniMind! We’re excited to see what you do with it. Let’s make MCP and AI easy and fun together!

— Lakshya Gupta & the OmniMind Team
