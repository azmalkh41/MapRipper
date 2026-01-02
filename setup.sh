#!/bin/bash
echo "Installing dependencies for Termux..."
pkg update && pkg upgrade -y
pkg install tur-repo -y
pkg install python python-pip chromium -y

# Install Python requirements
pip install flask selenium requests

echo "------------------------------------------------"
echo "Setup Complete!"
echo "To run the tool: python app.py"
echo "------------------------------------------------"
