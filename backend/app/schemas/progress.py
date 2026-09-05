from datetime import datetime

# Import the data model tool.
from pydantic import BaseModel, Field


class CompleteLessonRequest(BaseModel):
    # Read lesson completion data.
    lesson_code: str
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
