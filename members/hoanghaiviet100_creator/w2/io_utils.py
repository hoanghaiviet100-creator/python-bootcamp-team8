import csv
import json
from datetime import datetime
from .models import Task

def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2): # Dòng 1 là header
            try:
                title = row["title"].strip()
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = datetime.strptime(row["deadline"].strip(), "%Y-%m-%d").date()
                tasks.append(Task(title=title, importance=importance, effort_h=effort_h, deadline=deadline))
            except (KeyError, ValueError) as e:
                raise ValueError(f"Invalid row at line {line_num}: {e}")
    return tasks

def save_json(tasks: list[Task], path: str) -> None:
    data = []
    for t in tasks:
        data.append({
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat()
        })
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)