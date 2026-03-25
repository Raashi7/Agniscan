from agniscan.scanners.amass_scan import run_amass
from agniscan.scanners.nmap_scan import run_nmap
from agniscan.scanners.nikto_scan import run_nikto
from agniscan.scanners.sqlmap_scan import run_sqlmap
from agniscan.scanners.zap_scan import run_zap


def run_dast(target):

    print("\n[AgniScan] Starting DAST pipeline\n")

    try:

        print("[1/6] Running Amass (Subdomain Discovery)")
        run_amass(target)

        print("[2/6] Running Nmap (Port Scanning)")
        run_nmap(target)

        print("[3/6] Running Nikto (Web Server Scan)")
        run_nikto(target)

        print("[4/6] Running SQLMap (SQL Injection Testing)")
        run_sqlmap(target)

        print("[5/6] Running ZAP (Deep DAST Scan)")
        run_zap(target)

        print("\n[AgniScan] DAST scan completed successfully\n")

    except Exception as e:
        print(f"[!] DAST pipeline failed: {e}")
