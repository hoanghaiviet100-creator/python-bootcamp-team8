def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    timetable = {}
    for course, day in schedule:
        timetable.setdefault(day, []).append(course)
    
    # Sắp xếp danh sách các môn học theo thứ tự alphabet cho từng ngày
    for day in timetable:
        timetable[day].sort()
        
    return timetable