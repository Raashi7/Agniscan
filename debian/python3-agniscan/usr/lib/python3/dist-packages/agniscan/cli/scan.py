from agniscan.scanners.amass_scan import run_amass
from agniscan.scanners.nmap_scan import run_nmap
from agniscan.scanners.nikto_scan import run_nikto
from agniscan.ui.display import show_message


def run_full_scan(target):

    show_message("Starting Full Security Scan")

    run_amass(target)
    run_nmap(target)
    run_nikto(target)

    show_message("Full scan completed.")
