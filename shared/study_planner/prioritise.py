from datetime import date
from shared.contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    def priority_score(task: Task) -> float:
        days_left = (task.deadline - today).days
        return task.importance / max(days_left, 1)

    return sorted(tasks, key=priority_score, reverse=True)