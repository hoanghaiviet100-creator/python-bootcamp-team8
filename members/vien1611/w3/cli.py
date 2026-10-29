"""Command-line interface for the study planner."""

import argparse
import sys
from datetime import date
from pathlib import Path

from ..w2.io_utils import load_tasks
from ..w2.models import Task


def plan_tasks(
    tasks: list[Task], hours: float, today: date
) -> list[tuple[Task, float]]:
    """Allocate available study hours across tasks prioritised by urgency.

    Tasks are ordered by days left until deadline (ascending), importance (descending),
    and title (alphabetical).

    Parameters
    ----------
    tasks : list[Task]
        List of tasks to schedule.
    hours : float
        Available study hours.
    today : date
        Reference date for calculating days left.

    Returns
    -------
    list[tuple[Task, float]]
        List of (task, allocated_hours) pairs.
    """
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


def format_plan(plan: list[tuple[Task, float]], total_hours: float) -> str:
    """Format the study plan into a readable evening summary.

    Parameters
    ----------
    plan : list[tuple[Task, float]]
        Allocated task pairs.
    total_hours : float
        Total hours budgeted for the study session.

    Returns
    -------
    str
        Formatted study plan output string.
    """
    lines = [f"Tonight ({total_hours:.1f} h):"]
    if not plan:
        lines.append("  No tasks scheduled.")
        return "\n".join(lines)

    max_title_len = max(len(t.title) for t, _ in plan)
    pad_width = max(17, max_title_len + 4)

    for index, (task, allocated) in enumerate(plan, start=1):
        dot_count = max(3, pad_width - len(task.title) - 1)
        dots = "." * dot_count
        lines.append(f"  {index}. {task.title} {dots} {allocated:.1f} h")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """Parse command line arguments and output the nightly study plan.

    Parameters
    ----------
    argv : list[str] | None, default None
        List of command line arguments (defaults to sys.argv[1:]).

    Returns
    -------
    int
        Process exit code (0 on success, 1 on error).
    """
    parser = argparse.ArgumentParser(
        description="Generate an evening study plan from tasks CSV."
    )
    parser.add_argument("path", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours", type=float, required=True, help="Available study hours"
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date in YYYY-MM-DD format (defaults to current date)",
    )

    args = parser.parse_args(argv)

    if args.hours < 0:
        print("Error: --hours must be non-negative.", file=sys.stderr)
        return 1

    file_path = Path(args.path)
    if not file_path.exists():
        print(f"Error: file not found: {args.path}", file=sys.stderr)
        return 1

    try:
        ref_today = date.fromisoformat(args.today) if args.today else date.today()
    except ValueError:
        print(
            f"Error: invalid --today format: {args.today!r}. Expected YYYY-MM-DD.",
            file=sys.stderr,
        )
        return 1

    try:
        tasks = load_tasks(file_path)
    except (OSError, ValueError) as exc:
        print(f"Error loading tasks: {exc}", file=sys.stderr)
        return 1

    plan = plan_tasks(tasks, args.hours, ref_today)
    print(format_plan(plan, args.hours))
    return 0


if __name__ == "__main__":
    sys.exit(main())
