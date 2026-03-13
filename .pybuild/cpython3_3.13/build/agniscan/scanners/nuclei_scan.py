import subprocess

def run_nuclei(target):

    print("[+] Running Nuclei vulnerability scan")

    subprocess.run([
        "nuclei",
        "-u", target,
        "-t", "vulnerabilities/",
        "-severity", "medium,high,critical",
        "-silent",
        "-stats"
    ])
