import csv
from datetime import datetime

from shared.contract import Task


def parse_csv(path: str) -> list[Task]:
    """Đọc file CSV chứa danh sách task và chuyển thành danh sách các đối tượng Task chuẩn."""
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            task = Task(
                title=row["title"].strip(),
                importance=int(row["importance"]),
                effort_h=float(row["effort_h"]),
                deadline=datetime.strptime(row["deadline"].strip(), "%Y-%m-%d").date()
            )
            tasks.append(task)
    return tasks
