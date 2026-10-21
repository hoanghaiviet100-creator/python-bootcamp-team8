import csv
import json
import math
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from CSV and report invalid rows with line numbers."""
    tasks: list[Task] = []
    required_fields = ["title", "importance", "effort_h", "deadline"]

    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != required_fields:
            raise ValueError(
                "Invalid CSV header at line 1: expected "
                "title,importance,effort_h,deadline"
            )

        for row in reader:
            line_number = reader.line_num

            try:
                if None in row:
                    raise ValueError("too many columns")

                title = row["title"]
                importance_text = row["importance"]
                effort_text = row["effort_h"]
                deadline_text = row["deadline"]

                if any(
                    value is None
                    for value in (
                        title,
                        importance_text,
                        effort_text,
                        deadline_text,
                    )
                ):
                    raise ValueError("missing column value")

                title = title.strip()

                if not title:
                    raise ValueError("title cannot be empty")

                importance = int(importance_text)
                effort_h = float(effort_text)
                deadline = date.fromisoformat(deadline_text.strip())

                if not math.isfinite(effort_h) or effort_h < 0:
                    raise ValueError(
                        "effort_h must be a non-negative finite number"
                    )

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)

            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(
                    f"Invalid data at line {line_number}: {exc}"
                ) from exc

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks to JSON, converting dates into ISO strings."""
    data = []

    for task in tasks:
        task_dict = asdict(task)
        task_dict["deadline"] = task.deadline.isoformat()
        data.append(task_dict)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)