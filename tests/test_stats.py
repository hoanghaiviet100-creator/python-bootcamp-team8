"""Unit tests for stats.py."""

from datetime import date
from shared.contract import Task
from shared.study_planner.stats import compute_stats


def test_compute_stats_normal():
    today = date(2026, 10, 20)
    tasks = [
        Task("Task Overdue", 5, 2.5, date(2026, 10, 15)),
        Task("Task Today", 5, 1.5, date(2026, 10, 20)),
        Task("Task Future", 3, 4.0, date(2026, 10, 25)),
    ]

    res = compute_stats(tasks, today)

    assert res["total_tasks"] == 3
    assert res["total_effort_h"] == 8.0
    assert res["by_importance"] == {5: 2, 3: 1}
    assert res["by_status"] == {
        "overdue": 1,
        "due_today": 1,
        "upcoming": 1,
    }


def test_compute_stats_empty():
    today = date(2026, 10, 20)
    res = compute_stats([], today)

    assert res["total_tasks"] == 0
    assert res["total_effort_h"] == 0.0
    assert res["by_importance"] == {}
    assert res["by_status"] == {
        "overdue": 0,
        "due_today": 0,
        "upcoming": 0,
    }