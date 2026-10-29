from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    text = text.strip().lower()

    # Case 1: YYYY-MM-DD
    if text[0].isdigit():
        return date(int(text[0:4]), int(text[5:7]), int(text[8:10]))

    # Case 2: tomorrow
    elif text == "tomorrow":
        return today + timedelta(days=1)

    # Case 3: in N days
    elif text.startswith("in ") and text.endswith(" days"):
        days = int(text[3:-5])
        return today + timedelta(days=days)

    # Case 4: weekday names
    else:
        weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

        if text in weekdays:
            target = weekdays.index(text)
            days = (target - today.weekday()) % 7

            if days == 0:
                days = 7

            return today + timedelta(days=days)

    raise ValueError("Unknown date format")
