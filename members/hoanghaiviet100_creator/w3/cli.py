import argparse
from datetime import date
from pathlib import Path
import sys


def run_cli() -> None:
    parser = argparse.ArgumentParser(description="Task CLI Planner")
    parser.add_argument("csv_file", type=Path, help="Path to tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available study hours")
    parser.add_argument(
        "--today",
        type=str,
        default=str(date.today()),
        help="Date in YYYY-MM-DD format",
    )

    args = parser.parse_args()

    # Xử lý lỗi nếu file không tồn tại
    if not args.csv_file.exists():
        sys.stderr.write(f"Error: File '{args.csv_file}' not found.\n")
        sys.exit(1)

    try:
        today_date = date.fromisoformat(args.today)
    except ValueError:
        sys.stderr.write("Error: --today must be in YYYY-MM-DD format.\n")
        sys.exit(1)

    # Đọc file và hiển thị output định dạng mẫu
    print(f"Tonight ({args.hours:.1f} h):")
    with open(args.csv_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()][1:]  # Bỏ header
        for i, line in enumerate(lines, start=1):
            parts = line.split(",")
            title = parts[0].strip()
            dur = float(parts[1].strip())
            dots = "." * max(1, 15 - len(title))
            print(f"  {i}. {title} {dots} {dur:.1f} h")


if __name__ == "__main__":
    run_cli()