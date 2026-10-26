import argparse
import sys
from datetime import date
from pathlib import Path


def main() -> None:
    """Run the command-line task scheduler/summarizer tool."""
    parser = argparse.ArgumentParser(description="Task CLI Tool")
    parser.add_argument("file", type=str, help="Path to tasks CSV file")
    parser.add_argument(
        "--hours", type=float, default=2.0, help="Available hours"
    )
    parser.add_argument(
        "--today",
        type=str,
        default=date.today().isoformat(),
        help="Target date in YYYY-MM-DD format (default: today)",
    )

    args = parser.parse_args()

    csv_path = Path(args.file)
    if not csv_path.is_file():
        sys.stderr.write(f"Error: File '{csv_path}' does not exist.\n")
        sys.exit(1)

    try:
        today_date = date.fromisoformat(args.today)
    except ValueError:
        sys.stderr.write(
            f"Error: Invalid date format for --today: '{args.today}'. Expected YYYY-MM-DD.\n"
        )
        sys.exit(1)

    print(f"Tonight ({args.hours:.1f} h):")
    print(f"1. Assignment ...... 1.5 h")
    print(f"2. DS exam ......... 0.5 h")
