"""Load task CSV files and export task data as JSON."""

import csv
import json
from datetime import date

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Read task CSV data, raising ValueError with the invalid line number.

    Require the header title,importance,effort_h,deadline in that order.
    File access errors propagate to the caller.
    """
    tasks: list[Task] = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        expected_headers = [
            "title",
            "importance",
            "effort_h",
            "deadline",
        ]

        if reader.fieldnames != expected_headers:
            raise ValueError("Invalid CSV header at line 1")

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
                tasks.append(task)
            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(f"Invalid row at line {line_number}: {exc}") from exc

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Write tasks as UTF-8 JSON with ISO-formatted deadline strings."""
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
