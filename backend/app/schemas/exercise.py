# Import date and time values.
from datetime import datetime

# Import data model tools.
from pydantic import BaseModel, Field


class ExerciseAttemptRequest(BaseModel):
    # Read the student's answer.
    answer_text: str = Field(
        min_length=1,
        max_length=500,
    )

    # Read the time spent on this exercise.
    elapsed_seconds: int = Field(
        ge=0,
        le=3600,
    )


class ExerciseAttemptResponse(BaseModel):
    # Send the saved attempt ID.
    attempt_id: int

    # Send the lesson and exercise that were answered.
    lesson_code: str
    exercise_id: int

    # Tell the front if the answer was correct.
    is_correct: bool

    # Send clear feedback for the learner.
    feedback: str

    # Show the correct answer only after an incorrect attempt.
    correct_answer: str | None

    # Send when the attempt was saved.
    created_at: datetime
