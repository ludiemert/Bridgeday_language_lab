# Import the database session.
from backend.app.database import SessionLocal

# Import the lesson tables.
from backend.app.models import (
    Exercise,
    Lesson,
    LessonTranslation,
    VocabularyItem,
)

# Import the database search tool.
from sqlalchemy import select


def create_first_lesson() -> None:
    # Open the database session.
    database = SessionLocal()

    try:
        # Set a unique lesson code.
        lesson_code = "en-a2-work-routine-001"

        # Check if the lesson already exists.
        lesson_exists = database.scalar(
            select(Lesson).where(
                Lesson.lesson_code == lesson_code,
            ),
        )

        if lesson_exists:
            print("The first lesson already exists.")
            return

        # Create the first English lesson.
        lesson = Lesson(
            lesson_code=lesson_code,
            language_code="en",
            level_code="A2",
            topic="Work routine",
            category="daily_life",
            title="My work routine",
            text=(
                "Every morning, I check my schedule and make "
                "a short list of tasks. I answer important emails "
                "before my first meeting. This routine helps me "
                "start the day with a clear plan."
            ),
            grammar_note=(
                "Use the present simple for routines: " "I check, I make, I answer."
            ),
            estimated_minutes=10,
            status="published",
            translations=[
                LessonTranslation(
                    language_code="pt",
                    title="Minha rotina de trabalho",
                    text=(
                        "Todas as manhãs, eu verifico minha agenda "
                        "e faço uma pequena lista de tarefas. "
                        "Eu respondo e-mails importantes antes da "
                        "minha primeira reunião. Essa rotina me ajuda "
                        "a começar o dia com um plano claro."
                    ),
                    is_reviewed=True,
                ),
                LessonTranslation(
                    language_code="de",
                    title="Meine Arbeitsroutine",
                    text=(
                        "Jeden Morgen sehe ich meinen Kalender an "
                        "und mache eine kurze Aufgabenliste. "
                        "Ich beantworte wichtige E-Mails vor meinem "
                        "ersten Meeting. So beginne ich den Tag "
                        "mit einem klaren Plan."
                    ),
                    is_reviewed=True,
                ),
            ],
            vocabulary_items=[
                VocabularyItem(
                    target_word="schedule",
                    meaning_pt="agenda",
                    example_text="I check my schedule every morning.",
                    position=1,
                ),
                VocabularyItem(
                    target_word="task",
                    meaning_pt="tarefa",
                    example_text="I finish one task before lunch.",
                    position=2,
                ),
                VocabularyItem(
                    target_word="meeting",
                    meaning_pt="reunião",
                    example_text="My meeting starts at ten o'clock.",
                    position=3,
                ),
            ],
            exercises=[
                Exercise(
                    exercise_type="fill_blank",
                    question_text=(
                        "Complete the word:\n" "I check my s _ _ _ _ _ _ every morning."
                    ),
                    answer_text="schedule",
                    hint_text="It is your plan for the day.",
                    position=1,
                ),
            ],
        )

        # Save the lesson data.
        database.add(lesson)
        database.commit()

        print("The first lesson was created.")
    finally:
        # Close the database session.
        database.close()


if __name__ == "__main__":
    # Start the lesson script.
    create_first_lesson()
