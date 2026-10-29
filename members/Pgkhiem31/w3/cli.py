"""Build a personal study plan from the Week 2 CSV task format."""

import argparse
import sys
from collections.abc import Sequence
from datetime import date
from math import isfinite
from pathlib import Path

from ..w2.io_utils import load_tasks
from ..w2.models import Task


def positive_hours(text: str) -> float:
    """Parse a finite, positive number of available study hours."""
    try:
        hours = float(text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("hours must be a number") from exc
    if not isfinite(hours) or hours <= 0:
        raise argparse.ArgumentTypeError("hours must be finite and greater than 0")
    return hours


def iso_date(text: str) -> date:
    """Parse a calendar date and report invalid input through argparse."""
    try:
        parsed = date.fromisoformat(text)
        if parsed.isoformat() != text:
            raise ValueError("expected YYYY-MM-DD")
        return parsed
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "today must be a valid YYYY-MM-DD date"
        ) from exc


def priority_score(task: Task, today: date) -> float:
    """Rank due/overdue tasks first, then importance divided by days left."""
    days_left = task.days_left(today)
    return float("inf") if days_left == 0 else task.importance / days_left


def build_plan(
    tasks: Sequence[Task], hours: float, today: date
) -> list[tuple[Task, float]]:
    """Allocate the available hours in priority order, allowing a partial task.

    Equal priorities preserve CSV order. Invalid hours or task effort raise
    ValueError, including tasks that would fall outside the available time.
    """
    if not isfinite(hours) or hours <= 0:
        raise ValueError("Available hours must be finite and greater than 0")
    for task in tasks:
        if not isfinite(task.effort_h) or task.effort_h <= 0:
            raise ValueError(
                f"Effort for {task.title!r} must be finite and greater than 0"
            )

    ordered = sorted(tasks, key=lambda task: priority_score(task, today), reverse=True)
    plan: list[tuple[Task, float]] = []
    remaining = hours
    for task in ordered:
        if remaining <= 0:
            break
        allocated = min(task.effort_h, remaining)
        plan.append((task, allocated))
        remaining -= allocated
    return plan


def render(plan: Sequence[tuple[Task, float]], hours: float) -> str:
    """Format allocated tasks as a numbered evening study plan."""
    lines = [f"Tonight ({hours:.1f} h):"]
    for index, (task, allocated) in enumerate(plan, start=1):
        lines.append(f"  {index}. {task.title:.<24} {allocated:.1f} h")
    if not plan:
        lines.append("  No tasks to schedule.")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI; return 1 for CSV/file errors and 0 on success."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path", type=Path, help="CSV with title,importance,effort_h,deadline"
    )
    parser.add_argument(
        "--hours", required=True, type=positive_hours, help="available study hours"
    )
    parser.add_argument(
        "--today", type=iso_date, default=date.today(), help="reference date YYYY-MM-DD"
    )
    args = parser.parse_args(argv)

    try:
        tasks = load_tasks(args.path)
        plan = build_plan(tasks, args.hours, args.today)
    except FileNotFoundError:
        print(f"Error: file not found: {args.path}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(render(plan, args.hours))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
