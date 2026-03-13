from agniscan.scanners.amass_scan import run_amass
from agniscan.scanners.nmap_scan import run_nmap
from agniscan.scanners.nikto_scan import run_nikto
from agniscan.scanners.nuclei_scan import run_nuclei



def run_dast(target):

    print("[AgniScan] Starting DAST scan")

    try:
        from agniscan.scanners.zap_scan import run_zap
    except ImportError:
        print("[!] ZAP module not available")
        return

    run_zap(target)

    print("[AgniScan] Starting DAST scan")

    run_amass(target)

    run_nmap(target)

    run_nikto(target)

    run_nuclei(target)

    run_zap(target)

    print("[AgniScan] DAST scan completed")
