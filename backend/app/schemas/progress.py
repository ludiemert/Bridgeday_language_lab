# Import date and time values.
from datetime import datetime

# Import the data model tools.
from pydantic import BaseModel, Field


class CompleteLessonRequest(BaseModel):
    # Read lesson completion data.
    lesson_code: str

    # Limit study time to four hours per completion.
    study_seconds: int = Field(
        ge=0,
        le=14400,
    )


class LessonProgressResponse(BaseModel):
    # Send saved progress data.
    lesson_code: str
    status: str
    study_seconds: int
    completed_at: datetime
    next_review_at: datetime


class ProgressHistoryItemResponse(BaseModel):
    # Send one completed lesson in the student's history.
    lesson_code: str
    language_code: str
    level_code: str
    title: str
    study_seconds: int
    completed_at: datetime | None
    next_review_at: datetime | None
    writing_text: str | None


class ProgressHistoryResponse(BaseModel):
    # Send the history summary for one learning track.
    language_code: str
    completed_lessons: int
    study_seconds_total: int
    history: list[ProgressHistoryItemResponse]
