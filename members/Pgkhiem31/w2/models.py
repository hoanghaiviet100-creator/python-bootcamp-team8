"""Define the Task dataclass used by the personal study planner."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Store a task title, importance, effort in hours, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Reject importance values outside the inclusive range 1 to 5."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return days until the deadline, clamped to zero for overdue tasks."""
        return max(0, (self.deadline - today).days)
