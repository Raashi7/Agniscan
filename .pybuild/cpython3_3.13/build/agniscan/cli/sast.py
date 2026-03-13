from agniscan.scanners.bandit_scan import run_bandit
from agniscan.scanners.semgrep_scan import run_semgrep
from agniscan.ui.display import show_message


def run_sast(target):

    show_message("Starting SAST scan...")

    run_bandit(target)
    run_semgrep(target)

    show_message("SAST scan completed.")
