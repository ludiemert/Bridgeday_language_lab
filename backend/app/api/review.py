# This file provides BridgeDay review API routes.
# It lists scheduled reviews and completes a due review.

# Import date and time tools.
from datetime import datetime, timedelta, timezone

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

# Import database tables.
from ..models import Lesson, LessonProgress

# Import review response data.
from ..schemas.review import (
    ReviewCompletionResponse,
    ReviewLessonResponse,
    ReviewQueueResponse,
)

# Create the review routes.
router = APIRouter(
    prefix="/api/reviews",
    tags=["Review"],
)

# Read the login token.
bearer_scheme = HTTPBearer(auto_error=False)


# Convert SQLite times to UTC times.
def to_utc(value: datetime) -> datetime:
    # Add UTC when SQLite has no timezone.
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)

    # Send time in UTC.
    return value.astimezone(timezone.utc)


@router.get(
    "",
    response_model=ReviewQueueResponse,
)
def read_review_queue(
    language_code: str | None = None,
    credentials: HTTPAuthorizationCredentials | None = Depends(
        bearer_scheme,
    ),
    database: Session = Depends(get_db),
) -> ReviewQueueResponse:
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

    # Set the current UTC time.
    now = datetime.now(timezone.utc)

    # Find completed lessons for this user.
    progress_query = (
        select(
            Lesson,
            LessonProgress,
        )
        .join(
            LessonProgress,
            LessonProgress.lesson_id == Lesson.id,
        )
        .where(
            LessonProgress.user_id == user_id,
            LessonProgress.status == "completed",
        )
    )

    # Filter reviews by the selected real language track.
    if language_code:
        progress_query = progress_query.where(
            Lesson.language_code == language_code,
        )

    # Read completed lessons with review dates.
    progress_rows = database.execute(progress_query).all()

    # Create the review list.
    reviews: list[ReviewLessonResponse] = []

    # Check every completed lesson.
    for lesson, progress in progress_rows:
        # Skip lessons without a review date.
        if progress.next_review_at is None:
            continue

        # Convert the saved review time to UTC.
        review_at = to_utc(progress.next_review_at)

        # Add this lesson to the review queue.
        reviews.append(
            ReviewLessonResponse(
                lesson_code=lesson.lesson_code,
                language_code=lesson.language_code,
                level_code=lesson.level_code,
                title=lesson.title,
                next_review_at=review_at,
                is_due=review_at <= now,
            ),
        )

    # Put due reviews before upcoming reviews.
    reviews.sort(
        key=lambda review: (
            not review.is_due,
            review.next_review_at,
        ),
    )

    # Send all scheduled reviews.
    return ReviewQueueResponse(
        reviews=reviews,
    )


@router.post(
    "/{lesson_code}/complete",
    response_model=ReviewCompletionResponse,
)
def complete_review(
    lesson_code: str,
    credentials: HTTPAuthorizationCredentials | None = Depends(
        bearer_scheme,
    ),
    database: Session = Depends(get_db),
) -> ReviewCompletionResponse:
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

    # Find the published lesson.
    lesson = database.scalar(
        select(Lesson).where(
            Lesson.lesson_code == lesson_code,
            Lesson.status == "published",
        ),
    )

    # Stop when the lesson does not exist.
    if lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lesson was not found.",
        )

    # Find completed progress for this learner and lesson.
    progress = database.scalar(
        select(LessonProgress).where(
            LessonProgress.user_id == user_id,
            LessonProgress.lesson_id == lesson.id,
            LessonProgress.status == "completed",
        ),
    )

    # Stop when this lesson was not completed yet.
    if progress is None or progress.next_review_at is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No scheduled review was found for this lesson.",
        )

    # Set the current UTC time.
    now = datetime.now(timezone.utc)

    # Read the saved review time.
    review_at = to_utc(progress.next_review_at)

    # Stop when the review date has not arrived.
    if review_at > now:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This lesson is not ready for review yet.",
        )

    # Schedule the next review five days from now.
    progress.next_review_at = now + timedelta(days=5)

    # Save the new review date.
    database.commit()

    # Read the saved database values.
    database.refresh(progress)

    # Send the updated review schedule.
    return ReviewCompletionResponse(
        lesson_code=lesson.lesson_code,
        next_review_at=progress.next_review_at,
    )
