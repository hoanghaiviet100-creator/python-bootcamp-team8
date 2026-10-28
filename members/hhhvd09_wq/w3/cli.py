"""Build a nightly study plan from a CSV file."""

import argparse
import math
import sys
from datetime import date
from pathlib import Path

from ..w2.io_utils import load_tasks
from ..w2.models import Task


def plan_tasks(
    tasks: list[Task], hours: float, today: date
) -> list[tuple[Task, float]]:
    """Allocate time to tasks by deadline, importance, then title."""
    ordered = sorted(
        tasks,
        key=lambda task: (
            task.days_left(today),
            -task.importance,
            task.title.casefold(),
        ),
    )
    plan: list[tuple[Task, float]] = []
    remaining = hours
    for task in ordered:
        if remaining <= 0:
            break
        if task.effort_h <= 0:
            continue
        allocated = min(task.effort_h, remaining)
        plan.append((task, allocated))
        remaining -= allocated
    return plan


def main(argv: list[str] | None = None) -> int:
    """Read tasks, display allocated hours, and return a process exit code."""
    parser = argparse.ArgumentParser(description="Create a nightly study plan.")
    parser.add_argument("csv_path", type=Path, help="Path to a tasks CSV file")
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--today", type=str, default=None)
    args = parser.parse_args(argv)
    if not math.isfinite(args.hours) or args.hours < 0:
        print("Error: --hours must be non-negative and finite.", file=sys.stderr)
        return 1
    try:
        today = date.fromisoformat(args.today) if args.today else date.today()
        tasks = load_tasks(args.csv_path)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    plan = plan_tasks(tasks, args.hours, today)
    print(f"Tonight ({args.hours:.1f} h):")
    if not plan:
        print("  No tasks scheduled.")
    for index, (task, allocated) in enumerate(plan, start=1):
        print(f"  {index}. {task.title} ...... {allocated:.1f} h")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
