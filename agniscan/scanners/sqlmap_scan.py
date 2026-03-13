import subprocess


def run_sqlmap(target):

    print("[+] Running SQLMap scan")

    if not target.startswith("http"):
        target = "http://" + target

    try:

        subprocess.run([
            "sqlmap",
            "-u", target,
            "--batch",
            "--crawl", "2",
            "--random-agent"
        ])

    except Exception as e:
        print(f"[!] SQLMap scan failed: {e}")
