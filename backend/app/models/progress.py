from __future__ import annotations

from datetime import datetime, timezone

# Import database column tools.
from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)

# Import ORM tools.
from sqlalchemy.orm import Mapped, mapped_column

# Import the table base.
from ..database import Base


class LessonProgress(Base):
    # Set the database table name.
    __tablename__ = "lesson_progress"

    # Keep one progress record per lesson.
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "lesson_id",
            name="unique_user_lesson_progress",
        ),
    )

    # Create the progress ID.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Connect progress to one user.
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    # Connect progress to one lesson.
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id"),
        nullable=False,
    )

    # Save the lesson status.
    status: Mapped[str] = mapped_column(
        String(20),
        default="not_started",
        nullable=False,
    )

    # Save the study time in seconds.
    study_seconds: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # Save the first study time.
    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Save the lesson completion time.
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Save the next review time.
    next_review_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )


class ExerciseAttempt(Base):
    # Set the database table name.
    __tablename__ = "exercise_attempts"

    # Create the attempt ID.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Connect the attempt to one user.
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    # Connect the attempt to one lesson.
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id"),
        nullable=False,
    )

    # Connect the attempt to one exercise.
    exercise_id: Mapped[int] = mapped_column(
        ForeignKey("exercises.id"),
        nullable=False,
    )

    # Save the user answer.
    answer_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Save if the answer is correct.
    is_correct: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    # Save the answer time in seconds.
    elapsed_seconds: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # Save the attempt time.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )


class WritingEntry(Base):
    # Set the database table name.
    __tablename__ = "writing_entries"

    # Create the writing ID.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Connect the writing to one user.
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    # Connect the writing to one lesson.
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id"),
        nullable=False,
    )

    # Save the writing language.
    language_code: Mapped[str] = mapped_column(
        String(2),
        nullable=False,
    )

    # Save the user writing.
    text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Save the writing time.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
