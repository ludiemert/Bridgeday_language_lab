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

# Import progress data models.
from ..schemas.progress import (
    CompleteLessonRequest,
    LessonProgressResponse,
)

# Create the progress routes.
router = APIRouter(
    prefix="/api/progress",
    tags=["Progress"],
)

# Read the login token.
bearer_scheme = HTTPBearer(auto_error=False)


@router.post(
    "/complete",
    response_model=LessonProgressResponse,
)
def complete_lesson(
    data: CompleteLessonRequest,
    credentials: HTTPAuthorizationCredentials | None = Depends(
        bearer_scheme,
    ),
    database: Session = Depends(get_db),
) -> LessonProgressResponse:
    # Check if the token exists.
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login is required.",
        )

    # Read the user ID from the token.
    user_id = read_access_token(credentials.credentials)

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token.",
        )

    # Find the published lesson.
    lesson = database.scalar(
        select(Lesson).where(
            Lesson.lesson_code == data.lesson_code,
            Lesson.status == "published",
        ),
    )

    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lesson was not found.",
        )

    # Find old lesson progress.
    progress = database.scalar(
        select(LessonProgress).where(
            LessonProgress.user_id == user_id,
            LessonProgress.lesson_id == lesson.id,
        ),
    )

    # Set the current time.
    now = datetime.now(timezone.utc)

    if progress:
        # Update old lesson progress.
        progress.status = "completed"
        progress.study_seconds += data.study_seconds
        progress.completed_at = now
        progress.next_review_at = now + timedelta(days=5)
    else:
        # Create new lesson progress.
        progress = LessonProgress(
            user_id=user_id,
            lesson_id=lesson.id,
            status="completed",
            study_seconds=data.study_seconds,
            started_at=now,
            completed_at=now,
            next_review_at=now + timedelta(days=5),
        )
        database.add(progress)

    # Save the lesson progress.
    database.commit()
    database.refresh(progress)

    return LessonProgressResponse(
        lesson_code=lesson.lesson_code,
        status=progress.status,
        study_seconds=progress.study_seconds,
        completed_at=progress.completed_at,
        next_review_at=progress.next_review_at,
    )
