"""Run the Week 2 task package as a Python module."""

import sys
from pathlib import Path

from .io_utils import load_tasks


def main() -> int:
    """Load a sample CSV and print its tasks."""
    default_path = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"

    if len(sys.argv) > 2:
        print("Usage: python -m members.hhhvd09_wq.w2 [csv_path]")
        return 1

    csv_path = Path(sys.argv[1]) if len(sys.argv) == 2 else default_path

    try:
        tasks = load_tasks(csv_path)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if not tasks:
        print("No tasks found.")
        return 0

    print("Study Tasks")
    print("-" * 50)

    for index, task in enumerate(tasks, start=1):
        print(
            f"{index}. {task.title} | "
            f"Importance: {task.importance} | "
            f"Effort: {task.effort_h:g} h | "
            f"Deadline: {task.deadline.isoformat()}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())