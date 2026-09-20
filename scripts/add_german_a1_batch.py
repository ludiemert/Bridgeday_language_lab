# This script adds six reviewed German A1 lessons to BridgeDay source data.
# Run it once from the main project folder before running import_lessons.py.

# Import JSON tools.
import json

# Import safe file path tools.
from pathlib import Path

# Find the main project folder from the scripts folder.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Set the reviewed lesson source file.
DATA_FILE = PROJECT_ROOT / "data" / "lessons-reviewed.json"

# Set a recoverable backup file.
BACKUP_FILE = PROJECT_ROOT / "data" / "lessons-reviewed.before-german-a1.json"


# Store the six reviewed German A1 base lessons.
GERMAN_A1_LESSONS = [
    {
        "lesson_code": "de-a1-daily-introduction-001",
        "language_code": "de",
        "level_code": "A1",
        "topic": "Daily introduction",
        "category": "daily_life",
        "title": "Guten Morgen",
        "text": "Guten Morgen. Ich heiße Anna und ich lerne Deutsch. Ich wohne in London und arbeite von Montag bis Freitag. Am Morgen trinke ich Kaffee und beginne meinen Tag ruhig.",
        "grammar_note": "Use ich heiße to say your name. Use ich wohne in to say where you live.",
        "estimated_minutes": 10,
        "status": "published",
        "translations": [
            {
                "language_code": "pt",
                "title": "Bom dia",
                "text": "Bom dia. Meu nome é Anna e eu estudo alemão. Eu moro em Londres e trabalho de segunda a sexta-feira. De manhã, eu tomo café e começo meu dia com calma.",
                "is_reviewed": True,
            },
            {
                "language_code": "en",
                "title": "Good morning",
                "text": "Good morning. My name is Anna and I learn German. I live in London and work from Monday to Friday. In the morning, I drink coffee and start my day calmly.",
                "is_reviewed": True,
            },
        ],
        "vocabulary_items": [
            {
                "target_word": "Guten Morgen",
                "meaning_pt": "bom dia",
                "example_text": "Guten Morgen, wie geht es dir?",
                "position": 1,
            },
            {
                "target_word": "wohnen",
                "meaning_pt": "morar",
                "example_text": "Ich wohne in London.",
                "position": 2,
            },
            {
                "target_word": "arbeiten",
                "meaning_pt": "trabalhar",
                "example_text": "Ich arbeite von Montag bis Freitag.",
                "position": 3,
            },
        ],
        "exercises": [
            {
                "exercise_type": "fill_blank",
                "question_text": "Ergänze den Satz: Ich h _ _ ß e Anna.",
                "answer_text": "heiße",
                "hint_text": "Use this verb to say your name.",
                "position": 1,
            },
        ],
    },
    {
        "lesson_code": "de-a1-cafe-order-002",
        "language_code": "de",
        "level_code": "A1",
        "topic": "Ordering at a cafe",
        "category": "daily_life",
        "title": "Im Café",
        "text": "Ich bin in einem Café. Ich möchte einen Kaffee und ein kleines Brötchen, bitte. Die Kellnerin fragt: Möchten Sie noch etwas? Ich sage: Nein, danke. Das ist alles.",
        "grammar_note": "Use ich möchte for a polite order. Use bitte and danke to be polite.",
        "estimated_minutes": 10,
        "status": "published",
        "translations": [
            {
                "language_code": "pt",
                "title": "No café",
                "text": "Estou em um café. Eu gostaria de um café e um pãozinho, por favor. A garçonete pergunta: Você gostaria de mais alguma coisa? Eu digo: Não, obrigada. É só isso.",
                "is_reviewed": True,
            },
            {
                "language_code": "en",
                "title": "At the cafe",
                "text": "I am in a cafe. I would like a coffee and a small bread roll, please. The waitress asks: Would you like anything else? I say: No, thank you. That is all.",
                "is_reviewed": True,
            },
        ],
        "vocabulary_items": [
            {
                "target_word": "der Kaffee",
                "meaning_pt": "o café",
                "example_text": "Ich möchte einen Kaffee, bitte.",
                "position": 1,
            },
            {
                "target_word": "das Brötchen",
                "meaning_pt": "o pãozinho",
                "example_text": "Das Brötchen ist frisch.",
                "position": 2,
            },
            {
                "target_word": "möchte",
                "meaning_pt": "gostaria",
                "example_text": "Ich möchte etwas essen.",
                "position": 3,
            },
        ],
        "exercises": [
            {
                "exercise_type": "fill_blank",
                "question_text": "Ergänze den Satz: Ich m _ _ h t e einen Kaffee.",
                "answer_text": "möchte",
                "hint_text": "Use this word for a polite order.",
                "position": 1,
            },
        ],
    },
    {
        "lesson_code": "de-a1-ask-directions-003",
        "language_code": "de",
        "level_code": "A1",
        "topic": "Asking for directions",
        "category": "daily_life",
        "title": "Wo ist der Bahnhof?",
        "text": "Entschuldigung, wo ist der Bahnhof? Gehen Sie geradeaus und dann nach links. Der Bahnhof ist neben dem Supermarkt. Vielen Dank für Ihre Hilfe. Gern geschehen.",
        "grammar_note": "Use wo ist to ask where something is. Use geradeaus and links for directions.",
        "estimated_minutes": 10,
        "status": "published",
        "translations": [
            {
                "language_code": "pt",
                "title": "Onde fica a estação?",
                "text": "Com licença, onde fica a estação? Siga em frente e depois vire à esquerda. A estação fica ao lado do supermercado. Muito obrigada pela sua ajuda. De nada.",
                "is_reviewed": True,
            },
            {
                "language_code": "en",
                "title": "Where is the station?",
                "text": "Excuse me, where is the station? Go straight ahead and then turn left. The station is next to the supermarket. Thank you very much for your help. You are welcome.",
                "is_reviewed": True,
            },
        ],
        "vocabulary_items": [
            {
                "target_word": "der Bahnhof",
                "meaning_pt": "a estação de trem",
                "example_text": "Der Bahnhof ist in der Stadt.",
                "position": 1,
            },
            {
                "target_word": "geradeaus",
                "meaning_pt": "em frente",
                "example_text": "Gehen Sie geradeaus.",
                "position": 2,
            },
            {
                "target_word": "links",
                "meaning_pt": "à esquerda",
                "example_text": "Dann gehen Sie nach links.",
                "position": 3,
            },
        ],
        "exercises": [
            {
                "exercise_type": "fill_blank",
                "question_text": "Ergänze die Frage: Wo ist der B _ _ _ _ _ _?",
                "answer_text": "Bahnhof",
                "hint_text": "It is a train station.",
                "position": 1,
            },
        ],
    },
    {
        "lesson_code": "de-a1-supermarket-004",
        "language_code": "de",
        "level_code": "A1",
        "topic": "Shopping",
        "category": "daily_life",
        "title": "Im Supermarkt",
        "text": "Heute gehe ich in den Supermarkt. Ich kaufe Brot, Milch, Äpfel und Wasser. Die Äpfel sind frisch und die Milch ist kalt. An der Kasse bezahle ich mit Karte.",
        "grammar_note": "Use ich kaufe to say what you buy. Use mit Karte to say you pay by card.",
        "estimated_minutes": 10,
        "status": "published",
        "translations": [
            {
                "language_code": "pt",
                "title": "No supermercado",
                "text": "Hoje eu vou ao supermercado. Eu compro pão, leite, maçãs e água. As maçãs estão frescas e o leite está gelado. No caixa, pago com cartão.",
                "is_reviewed": True,
            },
            {
                "language_code": "en",
                "title": "At the supermarket",
                "text": "Today I go to the supermarket. I buy bread, milk, apples and water. The apples are fresh and the milk is cold. At the checkout, I pay by card.",
                "is_reviewed": True,
            },
        ],
        "vocabulary_items": [
            {
                "target_word": "das Brot",
                "meaning_pt": "o pão",
                "example_text": "Das Brot ist frisch.",
                "position": 1,
            },
            {
                "target_word": "die Milch",
                "meaning_pt": "o leite",
                "example_text": "Die Milch ist kalt.",
                "position": 2,
            },
            {
                "target_word": "bezahlen",
                "meaning_pt": "pagar",
                "example_text": "Ich bezahle mit Karte.",
                "position": 3,
            },
        ],
        "exercises": [
            {
                "exercise_type": "fill_blank",
                "question_text": "Ergänze den Satz: Ich k _ _ f e Brot und Milch.",
                "answer_text": "kaufe",
                "hint_text": "Use this verb when you buy something.",
                "position": 1,
            },
        ],
    },
    {
        "lesson_code": "de-a1-work-introduction-005",
        "language_code": "de",
        "level_code": "A1",
        "topic": "Introducing yourself at work",
        "category": "work",
        "title": "Mein erster Arbeitstag",
        "text": "Heute ist mein erster Arbeitstag. Ich treffe mein neues Team und stelle mich vor. Ich sage: Hallo, ich heiße Anna. Ich freue mich, hier zu arbeiten. Mein Team ist sehr freundlich.",
        "grammar_note": "Use ich heiße to introduce yourself. Use ich freue mich to say you are happy about something.",
        "estimated_minutes": 10,
        "status": "published",
        "translations": [
            {
                "language_code": "pt",
                "title": "Meu primeiro dia de trabalho",
                "text": "Hoje é meu primeiro dia de trabalho. Eu encontro minha nova equipe e me apresento. Eu digo: Olá, meu nome é Anna. Estou feliz em trabalhar aqui. Minha equipe é muito amigável.",
                "is_reviewed": True,
            },
            {
                "language_code": "en",
                "title": "My first day at work",
                "text": "Today is my first day at work. I meet my new team and introduce myself. I say: Hello, my name is Anna. I am happy to work here. My team is very friendly.",
                "is_reviewed": True,
            },
        ],
        "vocabulary_items": [
            {
                "target_word": "der Arbeitstag",
                "meaning_pt": "o dia de trabalho",
                "example_text": "Heute ist mein erster Arbeitstag.",
                "position": 1,
            },
            {
                "target_word": "das Team",
                "meaning_pt": "a equipe",
                "example_text": "Mein Team ist freundlich.",
                "position": 2,
            },
            {
                "target_word": "freundlich",
                "meaning_pt": "amigável",
                "example_text": "Die Kollegin ist sehr freundlich.",
                "position": 3,
            },
        ],
        "exercises": [
            {
                "exercise_type": "fill_blank",
                "question_text": "Ergänze den Satz: Mein T _ _ m ist freundlich.",
                "answer_text": "Team",
                "hint_text": "It is a group of people at work.",
                "position": 1,
            },
        ],
    },
    {
        "lesson_code": "de-a1-appointment-006",
        "language_code": "de",
        "level_code": "A1",
        "topic": "Making an appointment",
        "category": "daily_life",
        "title": "Ein Termin am Montag",
        "text": "Ich habe am Montag einen Termin beim Arzt. Der Termin ist um neun Uhr morgens. Ich nehme den Bus und bin zehn Minuten früher da. Nach dem Termin gehe ich nach Hause.",
        "grammar_note": "Use am for days: am Montag. Use um for time: um neun Uhr.",
        "estimated_minutes": 10,
        "status": "published",
        "translations": [
            {
                "language_code": "pt",
                "title": "Uma consulta na segunda-feira",
                "text": "Eu tenho uma consulta no médico na segunda-feira. A consulta é às nove horas da manhã. Eu pego o ônibus e chego dez minutos mais cedo. Depois da consulta, vou para casa.",
                "is_reviewed": True,
            },
            {
                "language_code": "en",
                "title": "An appointment on Monday",
                "text": "I have a doctor's appointment on Monday. The appointment is at nine o'clock in the morning. I take the bus and arrive ten minutes early. After the appointment, I go home.",
                "is_reviewed": True,
            },
        ],
        "vocabulary_items": [
            {
                "target_word": "der Termin",
                "meaning_pt": "o compromisso / a consulta",
                "example_text": "Ich habe einen Termin beim Arzt.",
                "position": 1,
            },
            {
                "target_word": "der Arzt",
                "meaning_pt": "o médico",
                "example_text": "Der Arzt ist freundlich.",
                "position": 2,
            },
            {
                "target_word": "früher",
                "meaning_pt": "mais cedo",
                "example_text": "Ich bin zehn Minuten früher da.",
                "position": 3,
            },
        ],
        "exercises": [
            {
                "exercise_type": "fill_blank",
                "question_text": "Ergänze den Satz: Ich habe am Montag einen T _ _ _ _ _.",
                "answer_text": "Termin",
                "hint_text": "It is an appointment.",
                "position": 1,
            },
        ],
    },
]


def add_german_a1_lessons() -> None:
    # Stop when the reviewed data file does not exist.
    if not DATA_FILE.exists():
        print("The reviewed lesson file was not found.")
        return

    # Read the current reviewed source data.
    with DATA_FILE.open(encoding="utf-8") as source_file:
        source_data = json.load(source_file)

    # Read the current lesson list.
    lessons = source_data.get("lessons", [])

    # Read existing lesson codes for safe repeated runs.
    existing_codes = {lesson["lesson_code"] for lesson in lessons}

    # Keep only German lessons not already in the source file.
    new_lessons = [
        lesson
        for lesson in GERMAN_A1_LESSONS
        if lesson["lesson_code"] not in existing_codes
    ]

    # Stop safely when this batch is already present.
    if not new_lessons:
        print("The German A1 lesson batch is already in the JSON file.")
        return

    # Create a backup before changing the source data.
    if not BACKUP_FILE.exists():
        BACKUP_FILE.write_text(
            json.dumps(source_data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    # Add all six German lessons to the current source list.
    lessons.extend(new_lessons)

    # Save the complete reviewed source file with readable formatting.
    source_data["lessons"] = lessons
    DATA_FILE.write_text(
        json.dumps(source_data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Show the completed source update.
    print(f"Added German A1 lessons: {len(new_lessons)}")
    print(f"Backup created: {BACKUP_FILE}")


if __name__ == "__main__":
    # Start the safe German A1 source update.
    add_german_a1_lessons()
