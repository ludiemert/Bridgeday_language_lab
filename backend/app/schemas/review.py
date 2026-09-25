# This file defines review API response data.

# Import date and time tools.
from datetime import datetime

# Import the data model tool.
from pydantic import BaseModel


class ReviewLessonResponse(BaseModel):
    # Send the lesson code.
    lesson_code: str

    # Send the real lesson language.
    language_code: str

    # Send the lesson level.
    level_code: str

    # Send the lesson title.
    title: str

    # Send the next scheduled review time.
    next_review_at: datetime

    # Tell if the learner can review now.
    is_due: bool


class ReviewQueueResponse(BaseModel):
    # Send due and upcoming review lessons.
    reviews: list[ReviewLessonResponse]


class ReviewCompletionResponse(BaseModel):
    # Send the reviewed lesson code.
    lesson_code: str

    # Send the next scheduled review time.
    next_review_at: datetime
