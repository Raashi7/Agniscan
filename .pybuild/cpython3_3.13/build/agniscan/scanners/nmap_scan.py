from urllib.parse import urlparse
import subprocess

def run_nmap(target):

    print("[+] Running Nmap scan")

    domain = urlparse(target).netloc or target

    subprocess.run([
        "nmap",
        "-sV",
        domain
    ])
