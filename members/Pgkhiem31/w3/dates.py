"""Parse absolute and relative task deadlines using the standard library."""

import re
from datetime import date, timedelta

_WEEKDAYS = {
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
    """Parse YYYY-MM-DD, tomorrow, in N days, or the next named weekday.

    Matching ignores surrounding whitespace and letter case. A weekday always
    refers to a future date, even when it matches today. Invalid expressions or
    dates outside the supported calendar raise ValueError.
    """
    value = text.strip().lower()
    try:
        if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
            return date.fromisoformat(value)
        if value == "tomorrow":
            return today + timedelta(days=1)
        relative = re.fullmatch(r"in\s+([0-9]+)\s+days?", value)
        if relative:
            return today + timedelta(days=int(relative.group(1)))
        if value in _WEEKDAYS:
            days = (_WEEKDAYS[value] - today.weekday()) % 7 or 7
            return today + timedelta(days=days)
    except (ValueError, OverflowError) as exc:
        raise ValueError(f"Invalid due date: {text!r}") from exc
    raise ValueError(f"Unknown due date: {text!r}")
