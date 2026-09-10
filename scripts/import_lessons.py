# This file imports reviewed BridgeDay lessons into SQLite.
# It reads one JSON file and saves only new lesson codes.

# Import JSON tools.
import json

# Import system path tools.
import sys

# Import safe file path tools.
from pathlib import Path

# Find the main project folder.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Let Python find the backend folder.
sys.path.insert(0, str(PROJECT_ROOT))

# Import the database session creator.
from backend.app.database import SessionLocal

# Import the lesson database tables.
from backend.app.models import (
    Exercise,
    Lesson,
    LessonTranslation,
    VocabularyItem,
)

# Import the database search tool.
from sqlalchemy import select

# Set the reviewed lesson file address.
DATA_FILE = PROJECT_ROOT / "data" / "lessons-reviewed.json"


def create_lesson(lesson_data: dict) -> Lesson:
    # Create one lesson with its translations, words, and exercises.
    return Lesson(
        lesson_code=lesson_data["lesson_code"],
        language_code=lesson_data["language_code"],
        level_code=lesson_data["level_code"],
        topic=lesson_data["topic"],
        category=lesson_data["category"],
        title=lesson_data["title"],
        text=lesson_data["text"],
        grammar_note=lesson_data.get("grammar_note"),
        estimated_minutes=lesson_data["estimated_minutes"],
        status=lesson_data["status"],
        translations=[
            LessonTranslation(
                language_code=translation["language_code"],
                title=translation["title"],
                text=translation["text"],
                is_reviewed=translation["is_reviewed"],
            )
            for translation in lesson_data["translations"]
        ],
        vocabulary_items=[
            VocabularyItem(
                target_word=item["target_word"],
                meaning_pt=item["meaning_pt"],
                example_text=item.get("example_text"),
                position=item["position"],
            )
            for item in lesson_data["vocabulary_items"]
        ],
        exercises=[
            Exercise(
                exercise_type=exercise["exercise_type"],
                question_text=exercise["question_text"],
                answer_text=exercise["answer_text"],
                hint_text=exercise.get("hint_text"),
                position=exercise["position"],
            )
            for exercise in lesson_data["exercises"]
        ],
    )


def import_reviewed_lessons() -> None:
    # Stop when the JSON file does not exist.
    if not DATA_FILE.exists():
        print("The reviewed lesson file was not found.")
        return

    # Open the JSON file with UTF-8 text.
    with DATA_FILE.open(encoding="utf-8") as source_file:
        source_data = json.load(source_file)

    # Read the lesson list.
    lessons = source_data.get("lessons", [])

    # Open the SQLite database session.
    database = SessionLocal()

    # Start the result counters.
    created_count = 0
    skipped_count = 0

    try:
        # Check every reviewed lesson.
        for lesson_data in lessons:
            # Read its unique code.
            lesson_code = lesson_data["lesson_code"]

            # Check if this lesson is already in SQLite.
            lesson_exists = database.scalar(
                select(Lesson).where(
                    Lesson.lesson_code == lesson_code,
                ),
            )

            # Skip lessons that already exist.
            if lesson_exists:
                print(f"Skipped existing lesson: {lesson_code}")
                skipped_count += 1
                continue

            # Create and prepare the new lesson.
            lesson = create_lesson(lesson_data)

            # Add it to the current database session.
            database.add(lesson)

            # Count the new lesson.
            created_count += 1

        # Save all new lessons together.
        database.commit()

        # Show a clear result.
        print(f"Created lessons: {created_count}")
        print(f"Skipped lessons: {skipped_count}")

    except (KeyError, TypeError, json.JSONDecodeError) as error:
        # Cancel incomplete work when source data has an error.
        database.rollback()

        # Show the source data problem.
        print(f"Import error: {error}")

    finally:
        # Close the database session.
        database.close()


if __name__ == "__main__":
    # Start the import when this file runs directly.
    import_reviewed_lessons()
