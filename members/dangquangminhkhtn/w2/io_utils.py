
import csv
import json
from datetime import date

from models import Task


def load_tasks(path: str) -> list[Task]:
    tasks = []

    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        expected_headers = ["title", "importance", "effort_h", "deadline"]

        if reader.fieldnames != expected_headers:
            raise ValueError("Invalid CSV header")

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"])
                )
                tasks.append(task)

            except (ValueError, TypeError, KeyError) as e:
                raise ValueError(
                    f"Invalid row at line {line_number}: {e}"
                ) from e

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    data = []

    for task in tasks:
        data.append({
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat()
        })

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
