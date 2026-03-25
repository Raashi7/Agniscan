from agniscan.scanners.bandit_scan import run_bandit
from agniscan.scanners.semgrep_scan import run_semgrep
from agniscan.ui.display import show_message

import os
import zipfile
import tempfile


def extract_zip(target):
    show_message("[+] ZIP file detected, extracting...")

    temp_dir = tempfile.TemporaryDirectory()

    try:
        with zipfile.ZipFile(target, 'r') as zip_ref:
            zip_ref.extractall(temp_dir.name)
    except zipfile.BadZipFile:
        show_message("[-] Error: Invalid or corrupted ZIP file")
        return None, None

    show_message(f"[+] Extracted to: {temp_dir.name}")
    return temp_dir.name, temp_dir


def run_sast(target):
    show_message("Starting SAST scan...")

    # ✅ FIX 1: absolute path
    target = os.path.abspath(target)

    show_message(f"[DEBUG] Target received: {target}")

    # Check if exists
    if not os.path.exists(target):
        show_message("[-] Error: Target not found")
        return

    scan_target = target
    temp_dir_obj = None

    # ✅ FIX 2: proper zip detection
    if target.lower().endswith(".zip"):
        extracted_path, temp_dir_obj = extract_zip(target)

        if extracted_path is None:
            return

        scan_target = extracted_path

    # Run scanners
    run_bandit(scan_target)
    run_semgrep(scan_target)

    show_message("SAST scan completed.")

    # Cleanup
    if temp_dir_obj:
        temp_dir_obj.cleanup()
        show_message("[+] Temporary files cleaned up")
