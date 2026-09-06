# Import the data model tool.
from pydantic import BaseModel


class DashboardResponse(BaseModel):
    # Send the current study streak.
    current_streak_days: int

    # Send lessons completed today.
    completed_today: int

    # Send lessons completed this week.
    completed_this_week: int

    # Send total study time in seconds.
    study_seconds_total: int

    # Send total completed lessons.
    total_completed_lessons: int

    # Send reviews that are ready now.
    reviews_due: int

    # Send completed lesson codes.
    completed_lesson_codes: list[str]
