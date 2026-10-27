import argparse
import sys
from datetime import date

from ..w2.io_utils import load_tasks
from shared.study_planner.prioritise import prioritise
from shared.study_planner.allocate import allocate


def main():
    parser = argparse.ArgumentParser(description="Study planner")

    parser.add_argument("file", help="Path to tasks CSV")
    parser.add_argument("--hours", type=float, required=True,
                        help="Available study hours")
    parser.add_argument("--today", type=date.fromisoformat,
                        default=date.today(),
                        help="Today's date (YYYY-MM-DD)")

    args = parser.parse_args()

    try:
        tasks = load_tasks(args.file)
    except FileNotFoundError:
        print(f"Error: file '{args.file}' not found", file=sys.stderr)
        sys.exit(1)

    ordered_tasks = prioritise(tasks, args.today)
    blocks = allocate(ordered_tasks, args.hours)

    total = sum(block.hours for block in blocks)

    print(f"Tonight ({total:.1f} h):")

    for i, block in enumerate(blocks, start=1):
        print(f"  {i}. {block.task.title} ...... {block.hours:.1f} h")


if __name__ == "__main__":
    main()
