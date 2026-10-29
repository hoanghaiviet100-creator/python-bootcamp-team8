
from ..contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Greedily allocate available hours to tasks in the given order."""
    if hours < 0:
        raise ValueError("Available hours cannot be negative.")

    blocks = []
    remaining_hours = hours

    for task in tasks:
        if remaining_hours <= 0:
            break

        if task.effort_h <= 0:
            continue

        allocated_hours = min(task.effort_h, remaining_hours)

        blocks.append(
            Block(task=task, hours=allocated_hours)
        )

        remaining_hours -= allocated_hours

    return blocks
