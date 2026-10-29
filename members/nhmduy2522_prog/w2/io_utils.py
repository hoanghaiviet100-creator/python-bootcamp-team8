import csv
import json
from datetime import date

from .models import Task


def load_tasks(path: str) -> list[Task]:
    """Đọc dữ liệu từ file CSV và chuyển đổi thành danh sách các đối tượng Task.

    Quăng lỗi ValueError kèm số dòng nếu dữ liệu không hợp lệ.
    """
    tasks = []

    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)

        header = next(reader, None)
        if header is None:
            return []

        for line_num, row in enumerate(reader, start=2):
            if not row:
                continue

            if len(row) != 4:
                raise ValueError(
                    f"line {line_num}: Expected 4 columns, got {len(row)}"
                )

            try:
                title = row[0].strip()
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = date.fromisoformat(row[3].strip())

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)

            except Exception as e:
                raise ValueError(f"Line {line_num}: {e}") from e

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    """Lưu danh sách các Task thành file JSON."""
    data = []
    for task in tasks:
        task_dict = {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        data.append(task_dict)

    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)