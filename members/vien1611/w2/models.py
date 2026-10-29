"""Data models for tasks."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represents a scheduled task with priority, effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate that importance is within the expected range 1 to 5."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Calculate the remaining days from today until deadline."""
        return max(0, (self.deadline - today).days)
