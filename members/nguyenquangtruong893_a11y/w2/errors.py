"""Custom exceptions and validation for study plan feasibility."""

from collections.abc import Iterable

from .models import Task


class InfeasiblePlan(Exception):
    """Exception raised when total needed hours exceed available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        message = (
            f"Plan is infeasible: needed {needed_h} hours, "
            f"but only {available_h} hours are available."
        )
        super().__init__(message)


def check_feasible(tasks: Iterable[Task], available_h: float) -> None:
    """Check if tasks can be completed within available hours.
    
    Raises InfeasiblePlan if total effort_h > available_h.
    """
    total_needed = sum(t.effort_h for t in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)