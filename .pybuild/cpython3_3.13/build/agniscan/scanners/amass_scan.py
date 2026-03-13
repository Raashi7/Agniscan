import subprocess


def run_amass(domain):

    print("[+] Running Amass subdomain discovery")

    try:
        result = subprocess.run(
            ["amass", "enum", "-passive", "-d", domain],
            capture_output=True,
            text=True
        )

        subdomains = result.stdout.splitlines()

        if not subdomains:
            print("[Amass] No subdomains found")
            return []

        print("\n[Amass] Subdomains Found:\n")

        for sub in subdomains:
            print(sub)

        return subdomains

    except Exception as e:
        print("[Amass Error]", e)
        return []
