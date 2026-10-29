import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse a date string into a date object.

    Accepts formats:
    - 'YYYY-MM-DD'
    - 'tomorrow'
    - 'in N days'
    - Weekday names like 'Fri', 'Friday' (returns the next occurrence)

    Raises ValueError if format is unknown.
    """
    clean_text = text.strip()

    # 1. ISO format: YYYY-MM-DD
    try:
        return date.fromisoformat(clean_text)
    except ValueError:
        pass

    # 2. 'tomorrow'
    if clean_text.lower() == "tomorrow":
        return today + timedelta(days=1)

    # 3. 'in X days'
    match = re.fullmatch(r"in\s+(\d+)\s+days?", clean_text, re.IGNORECASE)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    # 4. Weekday names (e.g. 'Fri', 'Friday')
    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    text_lower = clean_text.lower()

    target_idx = None
    for idx, day in enumerate(weekdays):
        if text_lower.startswith(day):
            target_idx = idx
            break

    if target_idx is not None:
        current_idx = today.weekday()
        # Tính khoảng cách ngày tới thứ tiếp theo (nếu trùng ngày hôm nay thì +7 ngày)
        days_ahead = (target_idx - current_idx) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Cannot parse date from text: '{text}'")