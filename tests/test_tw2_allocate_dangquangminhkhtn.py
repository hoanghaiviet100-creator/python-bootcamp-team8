
from datetime import date

import pytest

from shared.contract import Task, Block
from shared.study_planner.allocate import allocate


TODAY = date(2026, 10, 22)


def make_task(title: str, effort_h: float) -> Task:
    return Task(
        title=title,
        importance=3,
        effort_h=effort_h,
        deadline=TODAY,
    )


def test_allocate_all_tasks():
    tasks = [
        make_task("A", 2.0),
        make_task("B", 3.0),
    ]

    blocks = allocate(tasks, 5.0)

    assert len(blocks) == 2
    assert [block.hours for block in blocks] == [2.0, 3.0]


def test_allocate_partial_last_task():
    tasks = [
        make_task("A", 3.0),
        make_task("B", 4.0),
    ]

    blocks = allocate(tasks, 5.0)

    assert [block.hours for block in blocks] == [3.0, 2.0]
    assert sum(block.hours for block in blocks) == 5.0


def test_no_available_hours():
    tasks = [make_task("A", 2.0)]

    assert allocate(tasks, 0.0) == []


def test_empty_tasks():
    assert allocate([], 5.0) == []


def test_negative_hours_raises_error():
    tasks = [make_task("A", 2.0)]

    with pytest.raises(ValueError):
        allocate(tasks, -1.0)


def test_does_not_modify_original_tasks():
    tasks = [
        make_task("A", 2.0),
        make_task("B", 3.0),
    ]
    original = tasks.copy()

    allocate(tasks, 4.0)

    assert tasks == original


def test_skips_nonpositive_effort():
    tasks = [
        make_task("A", 0.0),
        make_task("B", 2.0),
    ]

    blocks = allocate(tasks, 3.0)

    assert len(blocks) == 1
    assert blocks[0].task.title == "B"
    assert blocks[0].hours == 2.0
