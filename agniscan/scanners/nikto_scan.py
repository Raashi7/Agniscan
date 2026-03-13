import subprocess

def run_nikto(target):

    if not target.startswith("http"):
        target = "http://" + target

    print("[+] Running Nikto web scan")

    subprocess.run([
        "nikto",
        "-h",
        target
    ])
