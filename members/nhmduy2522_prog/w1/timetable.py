def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Gộp các môn học theo từng thứ trong tuần (day):
    - Nhận vào danh sách các tuple (môn_học, thứ).
    - Trả về dictionary với key là thứ và value là danh sách tên môn học đã được sắp xếp[cite: 6].
    """
    result = {}
    
    for course, day in entries:
        result.setdefault(day, []).append(course)
        
    for day in result:
        result[day].sort()
        
    return result
