import subprocess


def run_bandit(target):

    print("[+] Running Bandit scan")

    subprocess.run([
        "bandit",
        "-r",
        target
    ])
