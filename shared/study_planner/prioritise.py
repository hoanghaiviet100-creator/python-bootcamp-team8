from datetime import date

from shared.contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    def priority_score(task: Task) -> float:
        days_left = (task.deadline - today).days

        if days_left <= 0:
            return float("inf")

        return task.importance / days_left

    return sorted(tasks, key=priority_score, reverse=True)
