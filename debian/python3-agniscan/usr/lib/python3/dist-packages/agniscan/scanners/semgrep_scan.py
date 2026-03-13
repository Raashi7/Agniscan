import subprocess

def run_semgrep(target):
    print("[+] Running Semgrep scan")

    try:
        subprocess.run([
            "semgrep",
            "--config=auto",
            target
        ])
    except FileNotFoundError:
        print("[!] Semgrep not installed. Skipping Semgrep scan.")
