import argparse

from agniscan.cli.sast import run_sast
from agniscan.cli.dast import run_dast


def main():

    logo = r"""
   ▄▄▄       ▄████  ███▄    █  ██▓  ██████  ▄████▄   ▄▄▄       ███▄    █
  ▒████▄    ██▒ ▀█▒ ██ ▀█   █ ▓██▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █
  ▒██  ▀█▄ ▒██░▄▄▄░▓██  ▀█ ██▒▒██▒░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
  ░██▄▄▄▄██░▓█  ██▓▓██▒  ▐▌██▒░██░  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
   ▓█   ▓██▒░▒▓███▀▒▒██░   ▓██░░██░▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
   ▒▒   ▓▒█░ ░▒   ▒ ░ ▒░   ▒ ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒
    ▒   ▒▒ ░  ░   ░ ░ ░░   ░ ▒░ ▒ ░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
    ░   ▒   ░ ░   ░    ░   ░ ░  ▒ ░░  ░  ░  ░          ░   ▒      ░   ░ ░
        ░  ░      ░          ░  ░        ░  ░ ░            ░  ░         ░

                🔥 AGNISCAN 🔥
"""

    parser = argparse.ArgumentParser(
        prog="agniscan",
        description=logo + "\nAutomated Security Scanner",
        formatter_class=argparse.RawTextHelpFormatter
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

    args = parser.parse_args()

    if args.command == "sast":
        run_sast(args.target)

    elif args.command == "dast":
        run_dast(args.target)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
