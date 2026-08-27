# This imports the JSON tool.
import json

# This imports file paths.
from pathlib import Path

# This imports the translation tool.
import argostranslate.translate

# This finds the main project folder.
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# This is the Portuguese lesson file.
INPUT_FILE = PROJECT_FOLDER / "data" / "lessons-pt.json"

# This is the translated lesson file.
OUTPUT_FILE = PROJECT_FOLDER / "data" / "lessons-translated.json"


# This translates one text.
def translate_text(text, target_language):
    # This translates from Portuguese.
    return argostranslate.translate.translate(text, "pt", target_language)


# This translates one lesson.
def translate_lesson(lesson):
    # This keeps the Portuguese lesson data.
    new_lesson = lesson.copy()

    # This creates English lesson data.
    english_lesson = {
        "title": translate_text(lesson["titlePt"], "en"),
        "text": translate_text(lesson["textPt"], "en"),
        "keywords": [translate_text(word, "en") for word in lesson["keywordsPt"]],
        "grammar": translate_text(lesson.get("grammarPt", ""), "en"),
        "speakingPrompt": translate_text(lesson.get("speakingPromptPt", ""), "en"),
    }

    # This creates German lesson data.
    german_lesson = {
        "title": translate_text(lesson["titlePt"], "de"),
        "text": translate_text(lesson["textPt"], "de"),
        "keywords": [translate_text(word, "de") for word in lesson["keywordsPt"]],
        "grammar": translate_text(lesson.get("grammarPt", ""), "de"),
        "speakingPrompt": translate_text(lesson.get("speakingPromptPt", ""), "de"),
    }

    # This adds both translations.
    new_lesson["translations"] = {"en": english_lesson, "de": german_lesson}

    # This shows that a person must check the text.
    new_lesson["needsReview"] = True

    # This sends back the new lesson.
    return new_lesson


# This runs the full translation.
def main():
    # This opens the Portuguese JSON file.
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        source_data = json.load(file)

    # This creates a list for new lessons.
    translated_lessons = []

    # This translates every lesson.
    for lesson in source_data["lessons"]:
        translated_lesson = translate_lesson(lesson)
        translated_lessons.append(translated_lesson)

    # This creates the final JSON data.
    output_data = {
        "project": source_data["project"],
        "sourceLanguage": source_data["sourceLanguage"],
        "lessons": translated_lessons,
    }

    # This saves the translated JSON file.
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(output_data, file, ensure_ascii=False, indent=2)

    # This shows a success message.
    print("Translation complete.")
    print("Lessons saved:", len(translated_lessons))
    print("File:", OUTPUT_FILE)


# This starts the script.
if __name__ == "__main__":
    main()
