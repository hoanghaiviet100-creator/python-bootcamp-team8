def can_register_thesis(credits:int,gpa:float)->bool:
    return bool(credits >= 120 and gpa >= 2.0)
def missing(credits:int,gpa:float)->list[str]:
    if can_register_thesis(credits,gpa):
        return []
    result=[]
    if credits<120:
        result.append(f"need {120-credits} more credits")
    if gpa<2.0:
        result.append(f"need {2.0-gpa:.2f} more gpa")
    return result