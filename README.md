# MapRipper
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/azmalkh41/MapRipper)

MapRipper is a web tool for extracting high-resolution images from Google Maps location pages. By providing a link to a specific place like a restaurant, park, or store, this application uses web scraping to find and display all associated images, allowing you to download them in a high-quality format.

The backend is built with Python and Flask, utilizing Selenium to navigate the dynamic, JavaScript-rendered content of Google Maps.

## Features

- **Extract from URL**: Simply paste a Google Maps location URL to get started.
- **High-Resolution Downloads**: Automatically retrieves higher-resolution versions of the images.
- **Simple Web Interface**: An easy-to-use interface for pasting links and viewing extracted images.
- **Termux Support**: Includes a setup script for quick installation and execution on Termux environments.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine, particularly if you are using Termux.

### Prerequisites

This tool is designed for a Linux-like environment. You will need the following packages installed:
- `python`
- `python-pip`
- `chromium`
- `git`

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/azmalkh41/MapRipper.git
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd MapRipper
    ```

3.  **Run the setup script:**
    This script will install the necessary dependencies for Termux.
    ```sh
    chmod +x setup.sh
    ./setup.sh
    ```

### Usage

1.  **Start the Flask server:**
    ```sh
    python app.py
    ```
    The server will start and be accessible on your local network at port 5000.

2.  **Access the Web Interface:**
    Open your web browser and navigate to `http://localhost:5000` (or `http://<your-device-ip>:5000` if accessing from another device on the same network).

3.  **Extract Images:**
    -   Find a location on Google Maps and copy its URL.
    -   Paste the URL into the input field on the MapRipper page.
    -   Click the **Extract Images** button and wait for the process to complete.
    -   The application will display all found images, which you can then download.
