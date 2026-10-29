"""I/O utility functions for loading and saving tasks."""

import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file.

    Parameters
    ----------
    path : str | Path
        Path to the CSV file.

    Returns
    -------
    list[Task]
        List of parsed Task objects.
    """
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2):
            try:
                title = row["title"].strip()
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"].strip())
                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)
            except (KeyError, ValueError, TypeError) as e:
                raise ValueError(f"Invalid row at line {line_num}: {e}") from e
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save a list of Task objects to a JSON file.

    Parameters
    ----------
    tasks : list[Task]
        List of tasks to serialize.
    path : str | Path
        Target destination JSON path.
    """
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat()
            if isinstance(t.deadline, date)
            else str(t.deadline),
        }
        for t in tasks
    ]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
