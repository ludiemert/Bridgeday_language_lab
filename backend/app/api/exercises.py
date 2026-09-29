# Import API route tools.
from fastapi import APIRouter, Depends, HTTPException, status

# Import token tools.
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# Import database search tools.
from sqlalchemy import select
from sqlalchemy.orm import Session

# Import token reader.
from ..core.security import read_access_token

# Import the database session.
from ..database import get_db

# Import exercise and lesson tables.
from ..models import Exercise, ExerciseAttempt, Lesson

# Import exercise request and response models.
from ..schemas.exercise import (
    ExerciseAttemptRequest,
    ExerciseAttemptResponse,
)

# Create exercise routes.
router = APIRouter(
    prefix="/api/exercises",
    tags=["Exercises"],
)

# Read the login token.
bearer_scheme = HTTPBearer(auto_error=False)


# Normalize answers without removing meaningful accents.
def normalize_answer(value: str) -> str:
    # Ignore letter case and extra spaces.
    return " ".join(value.casefold().split())


@router.post(
    "/{exercise_id}/attempts",
    response_model=ExerciseAttemptResponse,
)
def create_exercise_attempt(
    exercise_id: int,
    data: ExerciseAttemptRequest,
    credentials: HTTPAuthorizationCredentials | None = Depends(
        bearer_scheme,
    ),
    database: Session = Depends(get_db),
) -> ExerciseAttemptResponse:
    # Check if the token exists.
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login is required.",
        )

    # Read the user ID from the token.
    user_id = read_access_token(credentials.credentials)

    # Check if the token is valid.
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token.",
        )

    # Find one published lesson exercise.
    exercise_row = database.execute(
        select(
            Exercise,
            Lesson,
        )
        .join(
            Lesson,
            Lesson.id == Exercise.lesson_id,
        )
        .where(
            Exercise.id == exercise_id,
            Lesson.status == "published",
        ),
    ).first()

    # Stop when the exercise does not exist.
    if exercise_row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercise was not found.",
        )

    # Read the exercise and its lesson.
    exercise, lesson = exercise_row

    # Keep this first version focused on fill-in-the-blank exercises.
    if exercise.exercise_type != "fill_blank":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This exercise type is not supported yet.",
        )

    # Compare normalized answers.
    is_correct = normalize_answer(data.answer_text) == normalize_answer(
        exercise.answer_text
    )

    # Save the student's attempt.
    attempt = ExerciseAttempt(
        user_id=user_id,
        lesson_id=lesson.id,
        exercise_id=exercise.id,
        answer_text=data.answer_text,
        is_correct=is_correct,
        elapsed_seconds=data.elapsed_seconds,
    )
    database.add(attempt)

    # Save the attempt in SQLite.
    database.commit()
    database.refresh(attempt)

    # Send feedback for the learner.
    return ExerciseAttemptResponse(
        attempt_id=attempt.id,
        lesson_code=lesson.lesson_code,
        exercise_id=exercise.id,
        is_correct=is_correct,
        feedback=(
            "Correct! Great job."
            if is_correct
            else "Not quite. Check the correct answer and try again."
        ),
        correct_answer=(None if is_correct else exercise.answer_text),
        created_at=attempt.created_at,
    )
