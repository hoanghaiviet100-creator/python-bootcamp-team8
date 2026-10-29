"""W3-1: Date parsing utilities for deadlines and schedules."""

import re
from datetime import date, timedelta

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def parse_due(text: str, today: date) -> date:
    """Parse a date string into a date object relative to `today`.

    Accepts:
    - ISO format: "YYYY-MM-DD" (e.g. "2026-10-30")
    - Relative expressions: "tomorrow", "in <N> day(s)"
    - Weekday abbreviations: "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" (next occurrence)

    Raises:
        ValueError: If text does not match any accepted pattern.
    """
    clean_text = text.strip()
    if not clean_text:
        raise ValueError("Due date string cannot be empty")

    try:
        return date.fromisoformat(clean_text)
    except ValueError:
        pass

    lower_text = clean_text.lower()

    if lower_text == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in\s+(\d+)\s+days?", lower_text)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    for idx, day_name in enumerate(WEEKDAYS):
        if clean_text.capitalize() == day_name:
            current_weekday = today.weekday()
            days_ahead = (idx - current_weekday) % 7
            if days_ahead == 0:
                days_ahead = 7
            return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown or unsupported date format: {text!r}")
