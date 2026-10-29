from datetime import date

import pytest
from shared.study_planer.validate import validate_tasks

from shared.contract import Task


# 1. Trường hợp danh sách hợp lệ
def test_validate_tasks_success():
    tasks = [
        Task(title="DS exam", importance=5, effort_h=6.0, deadline=date(2026, 10, 30)),
        Task(title="Assignment", importance=4, effort_h=1.5, deadline=date(2026, 10, 27)),
    ]
    assert validate_tasks(tasks) is True


# 2. Báo lỗi khi danh sách rỗng
def test_validate_tasks_empty_list():
    with pytest.raises(ValueError, match="rỗng"):
        validate_tasks([])


# 3. Báo lỗi khi tiêu đề bị trống hoặc toàn khoảng trắng
def test_validate_tasks_empty_title():
    tasks = [Task(title="   ", importance=3, effort_h=2.0, deadline=date(2026, 10, 30))]
    with pytest.raises(ValueError, match="title"):
        validate_tasks(tasks)


# 4. Báo lỗi khi trùng lặp tiêu đề (không phân biệt hoa/thường)
def test_validate_tasks_duplicate_title():
    tasks = [
        Task(title="Math HW", importance=3, effort_h=2.0, deadline=date(2026, 10, 30)),
        Task(title="math hw", importance=4, effort_h=1.0, deadline=date(2026, 10, 31)),
    ]
    with pytest.raises(ValueError, match="trùng lặp"):
        validate_tasks(tasks)


# 5. Báo lỗi khi importance nằm ngoài khoảng 1-5
def test_validate_tasks_invalid_importance():
    tasks_too_low = [Task(title="Task A", importance=0, effort_h=2.0, deadline=date(2026, 10, 30))]
    tasks_too_high = [Task(title="Task B", importance=6, effort_h=2.0, deadline=date(2026, 10, 30))]

    with pytest.raises(ValueError, match="importance"):
        validate_tasks(tasks_too_low)

    with pytest.raises(ValueError, match="importance"):
        validate_tasks(tasks_too_high)


# 6. Báo lỗi khi effort_h <= 0
def test_validate_tasks_invalid_effort():
    tasks = [Task(title="Task A", importance=3, effort_h=0.0, deadline=date(2026, 10, 30))]
    with pytest.raises(ValueError, match="effort_h"):
        validate_tasks(tasks)


# 7. Báo lỗi khi deadline không phải kiểu datetime.date
def test_validate_tasks_invalid_deadline_type():
    tasks = [Task(title="Task A", importance=3, effort_h=2.0, deadline="2026-10-30")]  # type: ignore
    with pytest.raises(ValueError, match="deadline"):
        validate_tasks(tasks)