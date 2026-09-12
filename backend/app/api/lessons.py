# This file provides BridgeDay lesson API routes.
# It lists lessons, reads one lesson, and finds the next lesson.

# Import API route tools.
from fastapi import APIRouter, Depends, HTTPException, status

# Import login token tools.
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# Import database search tools.
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

# Import the token reader.
from ..core.security import read_access_token

# Import the database session.
from ..database import get_db

# Import lesson and progress tables.
from ..models import Lesson, LessonProgress

# Import lesson response models.
from ..schemas.lesson import (
    ExerciseResponse,
    LessonDetailResponse,
    LessonListResponse,
    LessonTranslationResponse,
    VocabularyResponse,
)

# Create the lesson routes.
router = APIRouter(
    prefix="/api/lessons",
    tags=["Lessons"],
)

# Read the optional login token.
bearer_scheme = HTTPBearer(auto_error=False)


def build_lesson_detail(lesson: Lesson) -> LessonDetailResponse:
    # Build the full lesson response.
    return LessonDetailResponse(
        lesson_code=lesson.lesson_code,
        language_code=lesson.language_code,
        level_code=lesson.level_code,
        topic=lesson.topic,
        category=lesson.category,
        title=lesson.title,
        text=lesson.text,
        grammar_note=lesson.grammar_note,
        estimated_minutes=lesson.estimated_minutes,
        translations=[
            LessonTranslationResponse(
                language_code=item.language_code,
                title=item.title,
                text=item.text,
                is_reviewed=item.is_reviewed,
            )
            for item in lesson.translations
        ],
        vocabulary_items=[
            VocabularyResponse(
                target_word=item.target_word,
                meaning_pt=item.meaning_pt,
                example_text=item.example_text,
                position=item.position,
            )
            for item in sorted(
                lesson.vocabulary_items,
                key=lambda item: item.position,
            )
        ],
        exercises=[
            ExerciseResponse(
                exercise_type=item.exercise_type,
                question_text=item.question_text,
                hint_text=item.hint_text,
                position=item.position,
            )
            for item in sorted(
                lesson.exercises,
                key=lambda item: item.position,
            )
        ],
    )


@router.get(
    "",
    response_model=list[LessonListResponse],
)
def list_lessons(
    language: str | None = None,
    level: str | None = None,
    database: Session = Depends(get_db),
) -> list[LessonListResponse]:
    # Start the lesson search.
    query = select(Lesson).where(
        Lesson.status == "published",
    )

    # Filter by language when needed.
    if language:
        query = query.where(
            Lesson.language_code == language,
        )

    # Filter by level when needed.
    if level:
        query = query.where(
            Lesson.level_code == level,
        )

    # Read the published lessons.
    lessons = database.scalars(
        query.order_by(Lesson.lesson_code),
    ).all()

    # Send lesson summary data.
    return [
        LessonListResponse(
            lesson_code=item.lesson_code,
            language_code=item.language_code,
            level_code=item.level_code,
            topic=item.topic,
            category=item.category,
            title=item.title,
            estimated_minutes=item.estimated_minutes,
        )
        for item in lessons
    ]


@router.get(
    "/next",
    response_model=LessonDetailResponse,
)
def read_next_lesson(
    credentials: HTTPAuthorizationCredentials | None = Depends(
        bearer_scheme,
    ),
    database: Session = Depends(get_db),
) -> LessonDetailResponse:
    # Stop when the user is not signed in.
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login is required.",
        )

    # Read the user ID from the login token.
    user_id = read_access_token(credentials.credentials)

    # Stop when the token is invalid.
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token.",
        )

    # Find lesson IDs already completed by this user.
    completed_lesson_ids = select(LessonProgress.lesson_id).where(
        LessonProgress.user_id == user_id,
        LessonProgress.status == "completed",
    )

    # Find the first published lesson not yet completed.
    lesson = database.scalars(
        select(Lesson)
        .options(
            selectinload(Lesson.translations),
            selectinload(Lesson.vocabulary_items),
            selectinload(Lesson.exercises),
        )
        .where(
            Lesson.status == "published",
            Lesson.id.not_in(completed_lesson_ids),
        )
        .order_by(Lesson.id),
    ).first()

    # Stop when every lesson is complete.
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No new lesson is available.",
        )

    # Send the next full lesson.
    return build_lesson_detail(lesson)


@router.get(
    "/{lesson_code}",
    response_model=LessonDetailResponse,
)
def read_lesson(
    lesson_code: str,
    database: Session = Depends(get_db),
) -> LessonDetailResponse:
    # Find one published lesson.
    lesson = database.scalar(
        select(Lesson)
        .options(
            selectinload(Lesson.translations),
            selectinload(Lesson.vocabulary_items),
            selectinload(Lesson.exercises),
        )
        .where(
            Lesson.lesson_code == lesson_code,
            Lesson.status == "published",
        ),
    )

    # Stop when the lesson does not exist.
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lesson was not found.",
        )

    # Send the full lesson.
    return build_lesson_detail(lesson)
