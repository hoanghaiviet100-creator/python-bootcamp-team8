"""I/O utilities for loading tasks from CSV and saving to JSON."""

import csv
import json
from datetime import date
from pathlib import Path
from typing import Any

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file.

    Expected CSV columns: title, importance, effort_h, deadline.
    Raises ValueError with the 1-based line number if any row is invalid.
    """
    tasks: list[Task] = []
    file_path = Path(path)

    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for line_num, row in enumerate(reader, start=1):
            if line_num == 1:
                # Bỏ qua dòng header
                continue
            if not row or not any(field.strip() for field in row):
                # Bỏ qua các dòng trống hoàn toàn nếu có
                continue
            if len(row) != 4:
                raise ValueError(
                    f"Invalid format at line {line_num}: expected 4 columns"
                )

            title, imp_str, effort_str, deadline_str = (item.strip() for item in row)
            try:
                importance = int(imp_str)
                effort_h = float(effort_str)
                deadline = date.fromisoformat(deadline_str)
                task = Task(title, importance, effort_h, deadline)
            except Exception as exc:
                raise ValueError(f"Invalid data at line {line_num}: {exc}") from exc

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save a list of Task objects to a JSON file."""
    file_path = Path(path)
    data: list[dict[str, Any]] = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]

    with open(file_path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
