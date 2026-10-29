"""Module for computing statistics, priority breakdown, and deadline status."""

from collections import Counter
from collections.abc import Iterable
from datetime import date
from typing import Any

from shared.contract import Task


def compute_stats(tasks: Iterable[Task], today: date) -> dict[str, Any]:
    """Thống kê tổng quan danh sách công việc.

    Trả về:
        - total_tasks: Tổng số lượng task.
        - total_effort_h: Tổng số giờ cần để hoàn thành tất cả task.
        - by_importance: Phân loại số lượng task theo mức độ ưu tiên (1-5).
        - by_status: Phân loại số lượng task theo trạng thái:
            + 'overdue': deadline < today
            + 'due_today': deadline == today
            + 'upcoming': deadline > today
    """
    task_list = list(tasks)
    total_tasks = len(task_list)
    total_effort_h = round(sum(t.effort_h for t in task_list), 2)


    by_importance = dict(Counter(t.importance for t in task_list))


    status_counter: Counter[str] = Counter()
    for t in task_list:
        if t.deadline < today:
            status_counter["overdue"] += 1
        elif t.deadline == today:
            status_counter["due_today"] += 1
        else:
            status_counter["upcoming"] += 1

    by_status = {
        "overdue": status_counter["overdue"],
        "due_today": status_counter["due_today"],
        "upcoming": status_counter["upcoming"],
    }

    return {
        "total_tasks": total_tasks,
        "total_effort_h": total_effort_h,
        "by_importance": by_importance,
        "by_status": by_status,
    }