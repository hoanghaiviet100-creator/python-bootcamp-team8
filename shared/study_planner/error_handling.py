class StudyPlannerError(Exception):
    """Base exception for all study planner errors."""
    pass


class InfeasiblePlan(StudyPlannerError):
    """Raised when the total task effort exceeds available study hours."""
    
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(self.__str__())

    def __str__(self) -> str:
        return (
            f"Plan is infeasible: need {self.needed_h} hours, "
            f"but only {self.available_h} hours are available."
        )


class EmptyFileError(StudyPlannerError, ValueError):
    """Raised when a task file is completely empty or missing headers."""
    pass