"""W3-3: Study planner command-line interface."""

import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import TextIO


@dataclass
class Task:
    """Task item representation."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def days_left(self, today: date) -> int:
        """Calculate days remaining until deadline (minimum 0)."""
        delta = (self.deadline - today).days
        return max(0, delta)


def load_tasks(path: Path) -> list[Task]:
    """Load tasks from a CSV file."""
    tasks: list[Task] = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2):
            try:
                title = row["title"].strip()
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"].strip())
                tasks.append(
                    Task(
                        title=title,
                        importance=importance,
                        effort_h=effort_h,
                        deadline=deadline,
                    )
                )
            except (KeyError, ValueError) as err:
                raise ValueError(f"Invalid row at line {line_num}: {err}") from err
    return tasks


def schedule_tasks(
    tasks: list[Task], available_hours: float, today: date
) -> list[tuple[Task, float]]:
    """Greedy scheduler: Sort by urgency (importance / days_left) and allocate hours."""
    sorted_tasks = sorted(
        tasks,
        key=lambda t: t.importance / max(t.days_left(today), 1),
        reverse=True,
    )

    allocated: list[tuple[Task, float]] = []
    remaining_hours = available_hours

    for task in sorted_tasks:
        if remaining_hours <= 0:
            break
        hours = min(task.effort_h, remaining_hours)
        allocated.append((task, hours))
        remaining_hours -= hours

    return allocated


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog="study_planner",
        description="Schedule study tasks based on available hours and task deadlines.",
    )
    parser.add_argument("csv_path", type=Path, help="Path to CSV file with tasks")
    parser.add_argument(
        "--hours", type=float, required=True, help="Available study hours"
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Anchor date in YYYY-MM-DD format (defaults to current date)",
    )
    return parser.parse_args(argv)


def run_cli(args: argparse.Namespace, out: TextIO = sys.stdout) -> int:
    """Execute CLI logic."""
    if not args.csv_path.is_file():
        sys.stderr.write(f"Error: File '{args.csv_path}' not found.\n")
        return 1

    try:
        today_date = date.fromisoformat(args.today) if args.today else date.today()
    except ValueError:
        sys.stderr.write(
            f"Error: Invalid --today date format '{args.today}'. Expected YYYY-MM-DD.\n"
        )
        return 1

    try:
        tasks = load_tasks(args.csv_path)
    except (ValueError, OSError, KeyError) as err:
        sys.stderr.write(f"Error reading CSV: {err}\n")
        return 1

    plan = schedule_tasks(tasks, args.hours, today_date)

    out.write(f"Tonight ({args.hours:.1f} h):\n")
    out.writelines(f"{idx}. {task.title:<15} {hours:.1f} h\n" for idx, (task, hours) in enumerate(plan, start=1))

    return 0

def main() -> None:
    """Entry point for CLI module."""
    args = parse_args()
    sys.exit(run_cli(args))


if __name__ == "__main__":
    main()
