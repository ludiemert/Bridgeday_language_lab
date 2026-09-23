# This file provides BridgeDay writing API routes.
# It saves and reads one learner sentence for each lesson.

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
from ..models import Lesson, WritingEntry

# Import writing data models.
from ..schemas.writing import (
    SaveWritingRequest,
    WritingEntryResponse,
)

# Create the writing routes.
router = APIRouter(
    prefix="/api/writing",
    tags=["Writing"],
)

# Read the login token.
bearer_scheme = HTTPBearer(auto_error=False)


@router.post(
    "",
    response_model=WritingEntryResponse,
)
def save_writing(
    data: SaveWritingRequest,
    credentials: HTTPAuthorizationCredentials | None = Depends(
        bearer_scheme,
    ),
    database: Session = Depends(get_db),
) -> WritingEntryResponse:
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

    # Remove extra spaces from the learner sentence.
    clean_text = data.text.strip()

    # Stop when the sentence has no real text.
    if not clean_text:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Write a sentence before saving.",
        )

    # Find the published lesson.
    lesson = database.scalar(
        select(Lesson).where(
            Lesson.lesson_code == data.lesson_code,
            Lesson.status == "published",
        ),
    )

    # Stop when the lesson does not exist.
    if lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lesson was not found.",
        )

    # Find the latest saved sentence for this user and lesson.
    writing_entry = database.scalar(
        select(WritingEntry)
        .where(
            WritingEntry.user_id == user_id,
            WritingEntry.lesson_id == lesson.id,
            WritingEntry.language_code == lesson.language_code,
        )
        .order_by(WritingEntry.id.desc()),
    )

    # Update the existing learner sentence.
    if writing_entry is not None:
        writing_entry.text = clean_text
    else:
        # Create the first learner sentence for this lesson.
        writing_entry = WritingEntry(
            user_id=user_id,
            lesson_id=lesson.id,
            language_code=lesson.language_code,
            text=clean_text,
        )
        database.add(writing_entry)

    # Save the writing entry.
    database.commit()

    # Read saved database values.
    database.refresh(writing_entry)

    # Send the saved learner sentence.
    return WritingEntryResponse(
        lesson_code=lesson.lesson_code,
        language_code=writing_entry.language_code,
        text=writing_entry.text,
    )


@router.get(
    "/{lesson_code}",
    response_model=WritingEntryResponse,
)
def read_writing(
    lesson_code: str,
    credentials: HTTPAuthorizationCredentials | None = Depends(
        bearer_scheme,
    ),
    database: Session = Depends(get_db),
) -> WritingEntryResponse:
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

    # Find the latest saved sentence for this user and lesson.
    writing_entry = database.scalar(
        select(WritingEntry)
        .where(
            WritingEntry.user_id == user_id,
            WritingEntry.lesson_id == lesson.id,
            WritingEntry.language_code == lesson.language_code,
        )
        .order_by(WritingEntry.id.desc()),
    )

    # Stop when the learner has not saved a sentence yet.
    if writing_entry is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No saved writing was found for this lesson.",
        )

    # Send the saved learner sentence.
    return WritingEntryResponse(
        lesson_code=lesson.lesson_code,
        language_code=writing_entry.language_code,
        text=writing_entry.text,
    )
