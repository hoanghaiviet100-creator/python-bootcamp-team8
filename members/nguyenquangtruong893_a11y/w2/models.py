"""Module defines Task model for study planner."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate task fields.
        
        Importance must be between 1 and 5 inclusive.
        """
        if not (1 <= self.importance <= 5):
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Calculate days remaining until deadline.
        
        Returns 0 if deadline has already passed (never below 0).
        """
        delta = (self.deadline - today).days
        return max(0, delta)