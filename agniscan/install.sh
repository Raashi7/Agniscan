#!/bin/bash

echo "[AgniScan] Installing dependencies..."

sudo apt update

echo "[+] Installing scanning tools..."

sudo apt install -y nmap
sudo apt install -y nikto
sudo apt install -y sqlmap
sudo apt install -y amass
sudo apt install -y golang

echo "[+] Installing Nuclei..."

go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

echo "[+] Updating Nuclei templates..."

nuclei -update-templates

echo "[+] Installing OWASP ZAP..."

sudo apt install -y zaproxy

echo "[+] Installing Python dependencies..."

pip install -r requirements.txt

echo "[✓] AgniScan installation completed"
