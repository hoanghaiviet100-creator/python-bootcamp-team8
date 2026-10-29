from datetime import date, timedelta
from shared.contract import Task
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise


def test_prioritise_ordering():
    today = date(2026, 10, 26)
    t1 = Task(title="Task A", importance=4, effort_h=2.0, deadline=today + timedelta(days=4))

    t2 = Task(title="Task B", importance=3, effort_h=1.0, deadline=today)
    
    result = prioritise([t1, t2], today)
    assert result[0].title == "Task B"
    assert result[1].title == "Task A"


def test_allocate_greedy():
    today = date(2026, 10, 26)
    t1 = Task(title="Task 1", importance=5, effort_h=2.0, deadline=today)
    t2 = Task(title="Task 2", importance=3, effort_h=3.0, deadline=today)
    

    blocks = allocate([t1, t2], hours=3.5)
    
    assert len(blocks) == 2
    assert blocks[0].hours == 2.0  
    assert blocks[1].hours == 1.5  