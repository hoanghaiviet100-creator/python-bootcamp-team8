"""Report when task effort exceeds the available study time."""

from collections.abc import Iterable

from .models import Task


class InfeasiblePlan(Exception):
    """Carry the required and available hours for an infeasible plan."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Store both hour totals and create a readable exception message."""
        self.needed_h = needed_h
        self.available_h = available_h

        super().__init__(
            f"Infeasible plan: need {needed_h} hours, "
            f"but only {available_h} hours available"
        )


def check_feasible(tasks: Iterable[Task], available_h: float) -> None:
    """Raise InfeasiblePlan when total task effort exceeds available hours."""
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
