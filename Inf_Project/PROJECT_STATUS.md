# BridgeDay — Project Status

## Project purpose

BridgeDay is a local daily language-learning application for English and German.

The learning method uses one main language at a time. The other language can be used for comparison.

## Current MVP status

The local MVP is working and ready for personal use.

| Area | Status |
| --- | --- |
| User registration and login | Complete |
| English and German language tracks | Complete |
| Lesson delivery from API | Complete |
| Grammar, vocabulary and writing areas | Complete |
| `fill_blank` exercises | Complete |
| Answer correction and saved attempts | Complete |
| Progress history by language | Complete |
| Spaced review | Complete |
| Lesson batch import | Complete |
| Mobile responsive layout | Complete |
| Local SQLite security in Git | Complete |

## Current learning tracks

| Language | Level | Lessons |
| --- | --- | ---: |
| Deutsch | A1 | 16 |
| English | A2 | 17 |
| **Total** | — | **33** |

## Main features

### Study

The Study page includes:

- Text;
- Listening;
- Grammar;
- Vocabulary;
- Speak & Write;
- a `fill_blank` practice exercise.

### Exercises

The current exercise engine supports:

```text
Exercise engine
├── fill_blank               # Implemented
├── multiple_choice          # Future
├── word_order               # Future
└── audio_comprehension      # Future
```

A learner can answer an exercise and receive:

- correct answer feedback;
- incorrect answer feedback;
- the expected answer when needed;
- a saved attempt in the database.

### Progress

Progress is separated by selected language.

It includes:

- completed lessons;
- study time;
- weekly activity;
- daily goal;
- total lessons;
- lesson history;
- future review dates.

### Spaced review

The review schedule is:

```text
1 day → 3 days → 7 days → 14 days → 30 days
```

A review cannot be completed before its planned date.

The API correctly returns `409 Conflict` for an early completion attempt.

## Architecture

```text
Browser
  ↓
Front-end: HTML, CSS and JavaScript
  ↓
FastAPI routes
  ↓
Schemas, services and security
  ↓
SQLAlchemy models
  ↓
SQLite database
```

## Important folders

```text
front/                  # Learner interface
backend/                # FastAPI application
data/                   # SQLite database and lesson batches
data/batches/           # Reviewed lesson JSON files
scripts/                # Import tools
info/                   # Internal project documentation
```

## Active database

The active local database is:

```text
data\bridgeday.db
```

This file contains the real local data and must not be deleted.

SQLite files are ignored by Git.

## Current migration

```text
b883e40f21a4 (head)
```

This migration includes the `review_count` field in `lesson_progress`.

## Completed validation

- FastAPI starts without errors.
- SQLite database is connected.
- Alembic migrations are current.
- Login was tested.
- Lessons load from the API.
- English and German tracks work.
- Correct and incorrect exercise answers were tested.
- Exercise attempts are saved.
- Progress history works by language.
- Review rules were tested.
- German A1 lesson batch was validated and imported.
- English A2 lesson batch was validated and imported.
- Mobile navigation shows Home, Study, Review and Progress.
- Local database files are not tracked by Git.

## Known limitations

The MVP is local and personal-use focused.

It does not yet include:

- public deployment;
- password recovery;
- full user profile editing;
- automated test suite;
- multiple-choice exercises;
- word-order exercises;
- audio-comprehension exercises;
- larger content library.

## Next development priorities

1. Create more reviewed lesson batches.
2. Add automated API tests.
3. Add multiple-choice exercises.
4. Add word-order exercises.
5. Add audio-comprehension exercises.
6. Improve user profile and validation.
7. Add password recovery.
8. Prepare public deployment.