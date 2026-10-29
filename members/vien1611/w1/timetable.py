"""Timetable organization functions."""


def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day in alphabetical order."""
    days = list(dict.fromkeys([item[1] for item in timetable]))
    result = {
        day: sorted([item[0] for item in timetable if item[1] == day]) for day in days
    }
    return result


if __name__ == "__main__":
    timetable_data = [("CSC10014", "Wed"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
    print(by_day(timetable_data))
