"""Date parsing utilities for bootcamp tasks."""

import re
from datetime import date, timedelta

_WEEKDAYS: dict[str, int] = {
    name: index
    for index, names in enumerate(
        (
            ("mon", "monday"),
            ("tue", "tuesday"),
            ("wed", "wednesday"),
            ("thu", "thursday"),
            ("fri", "friday"),
            ("sat", "saturday"),
            ("sun", "sunday"),
        )
    )
    for name in names
}


def parse_due(text: str, today: date) -> date:
    """Parse a task due date string relative to a given reference date.

    Supported formats:
    - ISO calendar date: "YYYY-MM-DD" (e.g. "2026-10-30")
    - Relative expression: "tomorrow"
    - Relative expression: "in N days" or "in N day"
    - Weekday name: "Mon", "Tue", ..., "Friday" (next occurrence, never today)

    Parameters
    ----------
    text : str
        The deadline description string.
    today : date
        The reference date.

    Returns
    -------
    date
        The resolved calendar due date.

    Raises
    ------
    ValueError
        If the text format is unrecognized or invalid.
    """
    cleaned = text.strip()
    lowered = cleaned.lower()

    # Case 1: ISO date (YYYY-MM-DD)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", lowered):
        try:
            return date.fromisoformat(lowered)
        except ValueError as exc:
            raise ValueError(f"Invalid calendar date: {text!r}") from exc

    # Case 2: "tomorrow"
    if lowered == "tomorrow":
        return today + timedelta(days=1)

    # Case 3: "in N days" / "in N day"
    rel_match = re.fullmatch(r"in\s+(\d+)\s+days?", lowered)
    if rel_match:
        days = int(rel_match.group(1))
        return today + timedelta(days=days)

    # Case 4: Weekday name (next occurrence strictly in the future)
    if lowered in _WEEKDAYS:
        target_weekday = _WEEKDAYS[lowered]
        days_ahead = (target_weekday - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown due date format: {text!r}")
