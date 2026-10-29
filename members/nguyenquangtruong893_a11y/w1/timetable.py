def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    timetable = {}
    for course, day in schedule:
        timetable.setdefault(day, []).append(course)
        
    
    for day in timetable:
        timetable[day].sort()
        
    return timetable