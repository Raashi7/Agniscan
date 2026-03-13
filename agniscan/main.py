import argparse

from agniscan.cli.sast import run_sast
from agniscan.cli.dast import run_dast
from agniscan.cli.scan import run_full_scan
from agniscan.cli.report import generate_report


def main():

    parser = argparse.ArgumentParser(
        prog="agniscan",
        description="AgniScan - Automated Security Scanner"
    )

    subparsers = parser.add_subparsers(dest="command")

    # ------------------------
    # SAST command
    # ------------------------
    sast_parser = subparsers.add_parser(
        "sast",
        help="Run Static Application Security Testing"
    )
    sast_parser.add_argument(
        "target",
        help="Source code directory"
    )

    # ------------------------
    # DAST command
    # ------------------------
    dast_parser = subparsers.add_parser(
        "dast",
        help="Run Dynamic Application Security Testing"
    )
    dast_parser.add_argument(
        "target",
        help="Target domain or IP"
    )

    # ------------------------
    # FULL SCAN
    # ------------------------
    scan_parser = subparsers.add_parser(
        "scan",
        help="Run full security scan"
    )
    scan_parser.add_argument(
        "target",
        help="Target domain or project"
    )

    # ------------------------
    # REPORT GENERATION
    # ------------------------
    report_parser = subparsers.add_parser(
        "report",
        help="Generate vulnerability report"
    )
    report_parser.add_argument(
        "file",
        help="Result JSON file"
    )

    args = parser.parse_args()

    if args.command == "sast":
        run_sast(args.target)

    elif args.command == "dast":
        run_dast(args.target)

    elif args.command == "scan":
        run_full_scan(args.target)

    elif args.command == "report":
        generate_report(args.file)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
