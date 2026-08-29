# This imports the JSON tool.
import json

# This reads private environment values.
import os

# This uses the DeepL translation service.
import deepl

# This loads the private .env file.
from dotenv import load_dotenv

# This imports file paths.
from pathlib import Path

# This finds the main project folder.
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# This is the Portuguese lesson file.
INPUT_FILE = PROJECT_FOLDER / "data" / "lessons-pt.json"

# This is the translated lesson file.
OUTPUT_FILE = PROJECT_FOLDER / "data" / "lessons-translated.json"

# This loads the private key from .env.
load_dotenv(PROJECT_FOLDER / ".env")

# This gets the private DeepL key.
DEEPL_AUTH_KEY = os.getenv("DEEPL_AUTH_KEY")

# This stops the program when the key is missing.
if not DEEPL_AUTH_KEY:
    raise ValueError("DEEPL_AUTH_KEY was not found in .env")

# This creates the DeepL translator.
translator = deepl.Translator(DEEPL_AUTH_KEY)

# This maps our app languages to DeepL languages.
TARGET_LANGUAGES = {"en": "EN-GB", "de": "DE"}


# This translates one text with DeepL.
def translate_text(text, target_language):
    # This avoids translating an empty text.
    if not text:
        return ""

    # This gets the DeepL target language.
    deepl_language = TARGET_LANGUAGES[target_language]

    # This sends the text to DeepL.
    result = translator.translate_text(
        text, source_lang="PT", target_lang=deepl_language
    )

    # This sends back the translated text.
    return result.text


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
