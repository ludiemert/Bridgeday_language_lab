# Import date and time tools.
from datetime import date, datetime, timedelta, timezone

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

# Import dashboard data model.
from ..schemas.dashboard import DashboardResponse

# Create the dashboard routes.
router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)

# Read the login token.
bearer_scheme = HTTPBearer(auto_error=False)


def to_utc(value: datetime) -> datetime:
    # Add UTC when SQLite has no timezone.
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)

    # Send time in UTC.
    return value.astimezone(timezone.utc)


def calculate_streak(
    completion_dates: set[date],
    today: date,
) -> int:
    # Start with no days.
    streak_days = 0

    # Start with today.
    check_date = today

    # Count days without a gap.
    while check_date in completion_dates:
        streak_days += 1
        check_date -= timedelta(days=1)

    # Send the total streak.
    return streak_days


@router.get(
    "",
    response_model=DashboardResponse,
)
def read_dashboard(
    credentials: HTTPAuthorizationCredentials | None = Depends(
        bearer_scheme,
    ),
    database: Session = Depends(get_db),
) -> DashboardResponse:
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

    # Find completed lessons for this user.
    progress_rows = database.execute(
        select(
            LessonProgress,
            Lesson.lesson_code,
        )
        .join(
            Lesson,
            Lesson.id == LessonProgress.lesson_id,
        )
        .where(
            LessonProgress.user_id == user_id,
            LessonProgress.status == "completed",
        ),
    ).all()

    # Set the current UTC time.
    now = datetime.now(timezone.utc)

    # Get the current date.
    today = now.date()

    # Find Monday for this week.
    week_start = today - timedelta(days=today.weekday())

    # Start dashboard totals.
    completed_today = 0
    completed_this_week = 0
    study_seconds_total = 0
    reviews_due = 0
    completion_dates: set[date] = set()
    completed_lesson_codes: list[str] = []

    # Read every completed lesson.
    for progress, lesson_code in progress_rows:
        # Add the lesson code.
        completed_lesson_codes.append(lesson_code)

        # Add saved study time.
        study_seconds_total += progress.study_seconds

        # Read the completion date.
        completed_at = to_utc(progress.completed_at)
        completed_date = completed_at.date()

        # Save the study date for the streak.
        completion_dates.add(completed_date)

        # Count lessons from today.
        if completed_date == today:
            completed_today += 1

        # Count lessons from this week.
        if completed_date >= week_start:
            completed_this_week += 1

        # Check if the review is ready.
        if progress.next_review_at is not None:
            review_at = to_utc(progress.next_review_at)

            if review_at <= now:
                reviews_due += 1

    # Send real dashboard data.
    return DashboardResponse(
        current_streak_days=calculate_streak(
            completion_dates,
            today,
        ),
        completed_today=completed_today,
        completed_this_week=completed_this_week,
        study_seconds_total=study_seconds_total,
        total_completed_lessons=len(progress_rows),
        reviews_due=reviews_due,
        completed_lesson_codes=completed_lesson_codes,
    )
