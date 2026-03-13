import subprocess


def run_semgrep(target):

    print("[+] Running Semgrep scan")

    subprocess.run([
        "semgrep",
        "--config=auto",
        target
    ])
