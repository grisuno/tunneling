# Simple Tunneling with Flask and python

# Tunneling

Tunneling is a simple web service that allows you to fetch and display web pages from other servers through a Flask application. It acts as a proxy to render the content of a given URL within an iframe.


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
    pip install Flask requests
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
