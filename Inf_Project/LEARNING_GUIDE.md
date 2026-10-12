# BridgeDay — Learning Guide

This file explains the main ideas learned while building BridgeDay.

## 1. What is BridgeDay?

BridgeDay is a local app for daily language study.

A learner can study English and German with:

- lessons;
- vocabulary;
- grammar;
- exercises;
- writing;
- progress;
- reviews.

BridgeDay is an MVP.

MVP means **Minimum Viable Product**. It is a small version of a product that is useful and working.

## 2. Front-end

The front-end is the part that the learner sees in the browser.

In BridgeDay, it is inside:

```text
front/
```

Important files:

| File | Purpose |
| --- | --- |
| `index.html` | Page structure |
| `styles.css` | Page style and mobile layout |
| `app.js` | Main page behavior |
| `js/exercises.js` | Exercise behavior |

## 3. HTML

HTML creates the page structure.

Example:

```html
<!-- A button lets the learner start an action. -->
<button type="button">Start lesson</button>

<!-- A section groups related content. -->
<section class="study-content">
  <h2>Grammar</h2>
</section>
```

Important ideas:

- `id` is a unique name for one HTML element.
- `class` is a reusable name for style or JavaScript.
- `hidden` hides an element.
- `button` creates a button.
- `section` groups page content.

## 4. CSS

CSS controls how the page looks.

Example:

```css
/* This styles the main menu. */
.main-nav {
  display: flex;
  gap: 6px;
}
```

Important ideas:

| CSS word | Meaning |
| --- | --- |
| `display: flex` | Puts items in a flexible line or column |
| `display: grid` | Puts items in rows and columns |
| `gap` | Space between items |
| `padding` | Space inside an element |
| `margin` | Space outside an element |
| `border-radius` | Rounded corners |
| `@media` | Style rules for smaller screens |

## 5. Responsive design

Responsive design means that the page works on phones, tablets, and computers.

On small phones, the BridgeDay menu uses two columns:

```text
Home     Study
Review   Progress
```

The front-end can be tested without the back-end when the goal is only to check the visual page.

## 6. JavaScript

JavaScript makes the page react to the learner.

It can:

- change English and German tracks;
- show the next lesson;
- call the API;
- show progress;
- send exercise answers;
- show correct or incorrect feedback.

Example:

```javascript
// Find a page element.
const grammarText = document.querySelector(".grammar-content .page-help");

// Change the text on the page.
grammarText.textContent = "Grammar will appear here.";
```

Important ideas:

| JavaScript word | Meaning |
| --- | --- |
| `const` | Saves a value or page element |
| `querySelector()` | Finds an HTML element |
| `textContent` | Changes visible text |
| `addEventListener()` | Waits for an action, like a click |
| `fetch()` | Sends a request to the API |
| `async` and `await` | Wait for an API response |

## 7. Back-end

The back-end is the Python part of the project.

It is inside:

```text
backend/
```

The back-end:

- receives requests from the front-end;
- checks data;
- protects passwords;
- reads the database;
- saves progress;
- checks exercise answers;
- plans reviews;
- sends data back to the browser.

## 8. FastAPI

FastAPI is the Python tool used to create the BridgeDay API.

The main application file is:

```text
backend/app/main.py
```

The API has routes such as:

```text
GET  /api/health
POST /api/auth/login
GET  /api/lessons/next
POST /api/exercises/{exercise_id}/attempts
GET  /api/progress/history
GET  /api/reviews
```

FastAPI documentation is here:

```text
http://127.0.0.1:8000/docs
```

The `/docs` page is for development and testing. It is not the learner page.

## 9. API

API means **Application Programming Interface**.

The API is the connection between the front-end and the database.

```text
Browser
  ↓
FastAPI API
  ↓
SQLite database
  ↓
API response
  ↓
Browser
```

Example:

```text
The front-end asks for the next lesson.
The API reads the database.
The API sends lesson data in JSON.
The front-end shows the lesson.
```

## 10. HTTP methods

| Method | Meaning |
| --- | --- |
| `GET` | Read data |
| `POST` | Create or send data |
| `PUT` | Update full data |
| `PATCH` | Update part of data |
| `DELETE` | Remove data |

Examples:

```text
GET  /api/lessons/next
POST /api/auth/login
POST /api/exercises/1/attempts
POST /api/reviews/lesson-code/complete
```

## 11. HTTP status codes

| Code | Meaning |
| ---:| --- |
| `200 OK` | The request worked |
| `201 Created` | A new item was created |
| `400 Bad Request` | The sent data is not correct |
| `401 Unauthorized` | Login is needed |
| `404 Not Found` | The route or data does not exist |
| `409 Conflict` | The action cannot happen now |
| `500 Internal Server Error` | The server has an internal problem |

In BridgeDay, `409 Conflict` is correct when a learner tries to complete a review too early.

## 12. JSON

JSON is a text format for data.

BridgeDay uses JSON for API responses and lesson batches.

Example:

```json
{
  "lesson_code": "de-a1-family-007",
  "language_code": "de",
  "level_code": "A1",
  "title": "Meine Familie"
}
```

Important JSON rules:

- JSON does not allow comments.
- Text uses double quotes.
- Commas must be correct.
- The file must be valid before import.

## 13. SQLite

SQLite is the local BridgeDay database.

The active file is:

```text
data\bridgeday.db
```

It stores data in tables.

Examples:

```text
users
lessons
lesson_translations
vocabulary_items
exercises
exercise_attempts
lesson_progress
writing_entries
```

SQLite is good for the MVP because it is free, simple, and uses one local file.

## 14. SQLAlchemy

SQLAlchemy connects Python to SQLite.

BridgeDay uses Python models instead of writing SQL everywhere.

```text
Python model
  ↓
SQLAlchemy
  ↓
SQLite table
```

The models are inside:

```text
backend/app/models/
```

## 15. Schemas

Schemas check the data sent to and from the API.

They are inside:

```text
backend/app/schemas/
```

Example:

```text
A login request sends email and password.
A schema checks if the data is complete and valid.
```

## 16. Login and security

BridgeDay uses:

- protected passwords;
- JWT tokens;
- user sessions;
- protected API routes.

Login flow:

```text
Learner sends email and password
  ↓
API checks the password
  ↓
API creates a token
  ↓
Browser saves the token
  ↓
Browser sends the token in protected requests
```

A password must never be saved as normal text.

## 17. CORS

The front-end uses port `5500`.

The back-end uses port `8000`.

CORS is a browser security rule that allows these two local addresses to work together.

```text
localhost:5500
  ↓
allowed request
  ↓
127.0.0.1:8000
```

## 18. Database migrations

A migration is a saved change to the database structure.

Example:

```text
Add review_count to lesson_progress
```

BridgeDay uses Alembic for migrations.

Flow:

```text
Change a Python database model
  ↓
Create a migration
  ↓
Check the migration file
  ↓
Apply the migration
  ↓
SQLite database is updated
```

Current migration:

```text
b883e40f21a4 (head)
```

## 19. Spaced review

Spaced review means that a lesson returns after some days.

BridgeDay review plan:

```text
1 day → 3 days → 7 days → 14 days → 30 days
```

The `review_count` value saves the number of completed reviews.

## 20. Lesson batches

Lesson batches are JSON files inside:

```text
data\batches/
```

Flow:

```text
Create a reviewed JSON file
  ↓
Validate JSON
  ↓
Run the import script
  ↓
Save new lessons in SQLite
  ↓
Show lessons in the app
```

The importer skips lesson codes that already exist.

## 21. Git

Git saves the history of the project.

| Git word | Meaning |
| --- | --- |
| Repository | Project folder with history |
| Commit | Saved project change |
| Branch | A line of work |
| `main` | Main project branch |
| `git status` | Shows local changes |
| `git add` | Prepares files for a commit |
| `git commit` | Saves a project change |
| `git push` | Sends commits to GitHub |

Safe Git flow:

```text
Change files
  ↓
git status --short
  ↓
git add specific-file
  ↓
git commit
  ↓
git push
```

## 22. .gitignore

`.gitignore` tells Git which local files must not go to GitHub.

BridgeDay ignores:

```text
.env
.venv/
*.db
*.db-shm
*.db-wal
__pycache__/
```

This protects private settings and local study data.

## 23. Beekeeper Studio

Beekeeper Studio is a visual tool for SQLite.

It can:

- show tables;
- show columns;
- run SQL;
- check saved data;
- help find database problems.

It is a development tool. The app still uses the API to read and save data.

## 24. Content quality rules

For good language lessons:

1. Write first in the study language.
2. Use the correct level, such as A1 or A2.
3. Write natural translations.
4. Check grammar and meaning.
5. Add useful vocabulary.
6. Add one good exercise.
7. Validate the JSON file.
8. Import the batch.
9. Test the lesson in the API and in the browser.

## 25. Main development rule

Use this process:

```text
Read first
  ↓
Understand the real problem
  ↓
Change one thing
  ↓
Test the result
  ↓
Save with Git
```

This helps protect the project and avoids changes based only on guesses.