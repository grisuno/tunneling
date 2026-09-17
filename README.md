# Simple Tunneling with Flask and python

# Tunneling

## Dont use in production environments, this it's app for practice pentesting, have an Full server-side request forgery in the line app.py:38 and it´s in debug mode. so... 

Insecure Tunneling is a simple web service that allows you to fetch and display web pages from other servers through a Flask application. It acts as a proxy to render the content of a given URL within an iframe. and to an atacker allow to Full server-side request forgery practice. like web pen testing activities.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)

## Features

- Fetch HTML content from any URL and render it within an iframe.
- Support for handling different content types.
- Easy to use and deploy.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/grisuno/tunneling.git
    cd tunneling
    ```

2. Install the required dependencies:
    ```sh
    chmod +x && ./install.sh
    ```

## Usage

1. Run the Flask application:
    ```sh
    python3 app.py
    ```

2. Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/?url=https://www.example.com
    ```

   Replace `https://www.example.com` with the URL you want to fetch and display.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Author

Grisuno

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Issues

If you encounter any issues, please create a new issue in the GitHub repository.


---
### Grisuno Offensive Security Ecosystem
This tool is part of a broader, synergistic RedTeam workflow:
- [LazyOwn](https://github.com/grisuno/LazyOwn): RedTeam/APT framework with AI-powered C&C, rootkits and malleable implants (Windows/Linux/Mac).
- [LazyOwnBT](https://github.com/grisuno/LazyOwnBT): Advanced complementary toolkit for BlueTeam professionals.
- [Lazymapd](https://github.com/grisuno/Lazymapd): Fast, customizable port scanner for firewall evasion.

<!-- readmenator-kb-link -->
## Knowledge Base

This project has been analyzed by [ReadMenator](https://github.com/grisuno/ReadMenator),
a zero-token polyglot static analysis tool. Analysis outputs are available:

- **[KNOWLEDGE_BASE.md](./KNOWLEDGE_BASE.md)** -- Full architecture reference with all
  classes, functions, imports, dependency graphs, UML class diagrams, security
  audit findings, community analysis, and more.
- **[readmenator-agent/](./readmenator-agent/)** -- Agent-friendly, grep-optimized index.
  - `INDEX.md` -- Quick reference: what each file does
  - `API.md` -- Public function contracts
  - `GOTCHAS.md` -- Change warnings
  - `SECURITY.md` -- Findings by severity
- **[readmenator-wiki/](./readmenator-wiki/)** -- Navigable wiki (start here for the big picture).
  - `index.md` -- Entry point: overview, reading order, god nodes, connections
  - `community_*.md` -- One synthesis page per code community
  - `REPORT.md` -- Honest audit: coverage, confidence, limits

AI agents: Read `readmenator-wiki/index.md` first for the big picture, then `readmenator-agent/INDEX.md` for grep-friendly lookup.
Developers: Read `KNOWLEDGE_BASE.md` for full architecture reference.
<!-- /readmenator-kb-link -->

