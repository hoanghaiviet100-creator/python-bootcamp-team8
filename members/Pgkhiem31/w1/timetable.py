#timetable.py
def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}

    for course, day in timetable:
        if day not in result:
            result[day] = []

        result[day].append(course)

    for day in result:
        result[day].sort()

    return result