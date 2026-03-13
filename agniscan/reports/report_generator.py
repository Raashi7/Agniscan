import json
import os

def create_report():

    report = {}

    files = {
        "bandit": "scan_results/bandit_results.json",
        "semgrep": "scan_results/semgrep_results.json"
    }

    for tool, file in files.items():

        if os.path.exists(file):

            with open(file) as f:
                report[tool] = json.load(f)

    with open("scan_results/final_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("[+] Report saved as scan_results/final_report.json")
