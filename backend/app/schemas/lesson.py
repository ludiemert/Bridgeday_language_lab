# Import the data model tool.
from pydantic import BaseModel


class LessonListResponse(BaseModel):
    # Send lesson summary data.
    lesson_code: str
    language_code: str
    level_code: str
    topic: str
    category: str
    title: str
    estimated_minutes: int


class LessonTranslationResponse(BaseModel):
    # Send one lesson translation.
    language_code: str
    title: str
    text: str
    is_reviewed: bool


class VocabularyResponse(BaseModel):
    # Send one vocabulary item.
    target_word: str
    meaning_pt: str
    example_text: str | None
    position: int


class ExerciseResponse(BaseModel):
    # Send one lesson exercise.
    exercise_type: str
    question_text: str
    hint_text: str | None
    position: int


class LessonDetailResponse(LessonListResponse):
    # Send full lesson data.
    text: str
    grammar_note: str | None
    translations: list[LessonTranslationResponse]
    vocabulary_items: list[VocabularyResponse]
    exercises: list[ExerciseResponse]
