import subprocess
import sys

def run_bandit(target):
    subprocess.run([
        sys.executable,
        "-m",
        "bandit",
        "-r",
        target
    ])
