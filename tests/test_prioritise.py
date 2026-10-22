
from datetime import date, timedelta

from shared.contract import Task
from shared.study_planner.prioritise import prioritise


TODAY = date(2026, 10, 22)


def make_task(
    title: str,
    importance: int,
    days_left: int,
) -> Task:
    return Task(
        title=title,
        importance=importance,
        effort_h=2.0,
        deadline=TODAY + timedelta(days=days_left),
    )


def test_sort_by_priority_score():
    tasks = [
        make_task("Python assignment", 4, 2),
        make_task("DS exam", 5, 1),
        make_task("English homework", 2, 4),
    ]

    result = prioritise(tasks, TODAY)

    assert [task.title for task in result] == [
        "DS exam",
        "Python assignment",
        "English homework",
    ]


def test_higher_importance_has_higher_priority():
    tasks = [
        make_task("Low importance", 1, 1),
        make_task("High importance", 5, 1),
    ]

    result = prioritise(tasks, TODAY)

    assert result[0].title == "High importance"


def test_closer_deadline_has_higher_priority():
    tasks = [
        make_task("Due in 5 days", 5, 5),
        make_task("Due tomorrow", 5, 1),
    ]

    result = prioritise(tasks, TODAY)

    assert result[0].title == "Due tomorrow"


def test_deadline_today_does_not_divide_by_zero():
    tasks = [
        make_task("Due tomorrow", 5, 1),
        make_task("Due today", 5, 0),
    ]

    result = prioritise(tasks, TODAY)

    assert result[0].title == "Due today"


def test_overdue_task_is_handled():
    tasks = [
        make_task("Due tomorrow", 5, 1),
        make_task("Overdue", 4, -2),
    ]

    result = prioritise(tasks, TODAY)

    assert result[0].title == "Overdue"


def test_equal_scores_keep_original_order():
    tasks = [
        make_task("First task", 2, 2),
        make_task("Second task", 4, 4),
    ]

    result = prioritise(tasks, TODAY)

    assert [task.title for task in result] == [
        "First task",
        "Second task",
    ]


def test_empty_list():
    assert prioritise([], TODAY) == []


def test_input_list_is_not_modified():
    tasks = [
        make_task("Low priority", 1, 5),
        make_task("High priority", 5, 1),
    ]
    original = tasks.copy()

    prioritise(tasks, TODAY)

    assert tasks == original
