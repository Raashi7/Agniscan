#!/bin/bash

echo "[+] Installing AgniScan..."

# Create virtual environment
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install CLI tool
pip install .

echo ""
echo "[✓] Installation Complete"
echo ""
echo "Run AgniScan using:"
echo ""
echo "source venv/bin/activate"
echo "agniscan dast example.com"
