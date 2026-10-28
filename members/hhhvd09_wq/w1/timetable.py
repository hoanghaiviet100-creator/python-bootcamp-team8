def by_day(items: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group and alphabetically sort course names for each weekday."""
    result = {}

    for course, day in items:
        result.setdefault(day, []).append(course)

    for course in result.values():
        course.sort()

    return result
