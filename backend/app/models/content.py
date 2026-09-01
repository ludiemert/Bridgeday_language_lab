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
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Import the table base.
from ..database import Base


class Lesson(Base):
    # Set the database table name.
    __tablename__ = "lessons"

    # Create the lesson ID.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Save a unique lesson code.
    lesson_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=False,
    )

    # Save the main study language.
    language_code: Mapped[str] = mapped_column(
        String(2),
        nullable=False,
    )

    # Save the lesson level.
    level_code: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    # Save the lesson topic.
    topic: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    # Save the lesson category.
    category: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    # Save the lesson title.
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Save the main lesson text.
    text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Save a small grammar note.
    grammar_note: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Save the study time in minutes.
    estimated_minutes: Mapped[int] = mapped_column(
        Integer,
        default=10,
        nullable=False,
    )

    # Save the content status.
    status: Mapped[str] = mapped_column(
        String(20),
        default="draft",
        nullable=False,
    )

    # Save the lesson creation time.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Connect translations to this lesson.
    translations: Mapped[list["LessonTranslation"]] = relationship(
        back_populates="lesson",
        cascade="all, delete-orphan",
    )

    # Connect words to this lesson.
    vocabulary_items: Mapped[list["VocabularyItem"]] = relationship(
        back_populates="lesson",
        cascade="all, delete-orphan",
    )

    # Connect exercises to this lesson.
    exercises: Mapped[list["Exercise"]] = relationship(
        back_populates="lesson",
        cascade="all, delete-orphan",
    )


class LessonTranslation(Base):
    # Set the database table name.
    __tablename__ = "lesson_translations"

    # Keep one translation per language.
    __table_args__ = (
        UniqueConstraint(
            "lesson_id",
            "language_code",
            name="unique_lesson_translation",
        ),
    )

    # Create the translation ID.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Connect the translation to a lesson.
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id"),
        nullable=False,
    )

    # Save the translation language.
    language_code: Mapped[str] = mapped_column(
        String(2),
        nullable=False,
    )

    # Save the translated title.
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Save the translated text.
    text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Mark a reviewed translation.
    is_reviewed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    # Connect this translation to a lesson.
    lesson: Mapped["Lesson"] = relationship(
        back_populates="translations",
    )


class VocabularyItem(Base):
    # Set the database table name.
    __tablename__ = "vocabulary_items"

    # Create the word ID.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Connect the word to a lesson.
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id"),
        nullable=False,
    )

    # Save the target word.
    target_word: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    # Save the Portuguese meaning.
    meaning_pt: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Save one word example.
    example_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Save the word order.
    position: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    # Connect this word to a lesson.
    lesson: Mapped["Lesson"] = relationship(
        back_populates="vocabulary_items",
    )


class Exercise(Base):
    # Set the database table name.
    __tablename__ = "exercises"

    # Create the exercise ID.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Connect the exercise to a lesson.
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id"),
        nullable=False,
    )

    # Save the exercise type.
    exercise_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    # Save the exercise question.
    question_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Save the correct answer.
    answer_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Save a small exercise hint.
    hint_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Save the exercise order.
    position: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    # Connect this exercise to a lesson.
    lesson: Mapped["Lesson"] = relationship(
        back_populates="exercises",
    )
