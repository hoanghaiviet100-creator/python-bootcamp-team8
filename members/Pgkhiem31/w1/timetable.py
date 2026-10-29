"""Group course names by their scheduled day."""


def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group (course, day) pairs by day and sort each course list."""
    result: dict[str, list[str]] = {}

    for course, day in timetable:
        if day not in result:
            result[day] = []

        result[day].append(course)

    for day in result:
        result[day].sort()

    return result
