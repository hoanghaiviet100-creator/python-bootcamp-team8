from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represent a study task with importance, effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate task importance after initialization."""
        if (
            isinstance(self.importance, bool)
            or not isinstance(self.importance, int)
            or not 1 <= self.importance <= 5
        ):
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return days until the deadline, never below zero."""
        return max(0, (self.deadline - today).days)