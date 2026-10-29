import re
from datetime import date, timedelta

WEEKDAYS = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}


def parse_due(text: str, today: date) -> date:
    """Parse a due date string relative to 'today'.

    Accepts ISO dates ('2026-10-30'), 'tomorrow', 'in X days',
    and weekday names like 'Fri' (next occurrence).
    Raises ValueError for unknown formats.
    """
    clean_text = text.strip().lower()

    # 1. Định dạng chuẩn YYYY-MM-DD
    try:
        return date.fromisoformat(text.strip())
    except ValueError:
        pass

    # 2. 'tomorrow'
    if clean_text == "tomorrow":
        return today + timedelta(days=1)

    # 3. 'in X days'
    match = re.match(r"^in\s+(\d+)\s+days?$", clean_text)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    # 4. Tên thứ trong tuần (ví dụ: 'Fri', 'Friday')
    day_prefix = clean_text[:3]
    if day_prefix in WEEKDAYS:
        target_wd = WEEKDAYS[day_prefix]
        days_ahead = (target_wd - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7  # Lấy ngày tương ứng ở tuần kế tiếp
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown due date format: '{text}'")