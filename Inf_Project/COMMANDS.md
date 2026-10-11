# BridgeDay — Commands Guide

This file contains the current useful commands for running, checking, maintaining, and extending BridgeDay.

Run every command from the main project folder:

```text
C:\Users\user\Downloads\Bridgeday_language_lab
```

## 1. Check the current folder

```powershell
# Show the folder where the terminal is currently running.
Get-Location
```

Expected folder:

```text
C:\Users\user\Downloads\Bridgeday_language_lab
```

## 2. Activate the Python environment

```powershell
# Activate the local Python virtual environment for this terminal.
.\.venv\Scripts\Activate.ps1
```

When active, PowerShell shows:

```text
(.venv)
```

Using the full path `.\.venv\Scripts\python.exe` also works without activating the environment.

## 3. Start the front-end

```powershell
# Serve the exact front folder used by the browser.
.\.venv\Scripts\python.exe -m http.server 5500 --directory front
```

Open:

```text
http://localhost:5500
```

Keep this terminal open while using the interface.

## 4. Start the back-end API

```powershell
# Start FastAPI and reload automatically after Python changes.
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload
```

Useful addresses:

```text
http://127.0.0.1:8000/api/health
http://127.0.0.1:8000/docs
```

- `/api/health` checks whether the API is running.
- `/docs` opens FastAPI interactive documentation.

Stop either server with:

```text
Ctrl + C
```

## 5. Check Python syntax

```powershell
# Check Python syntax without starting the API.
.\.venv\Scripts\python.exe -m compileall backend
```

A successful result lists Python files without `SyntaxError` or `Traceback`.

## 6. Check the active database migration

```powershell
# Show the migration applied to the active SQLite database.
.\.venv\Scripts\python.exe -m alembic current
```

Current expected result:

```text
b883e40f21a4 (head)
```

## 7. Apply pending database migrations

```powershell
# Apply every migration not yet applied to SQLite.
.\.venv\Scripts\python.exe -m alembic upgrade head
```

Use this after a new migration file is reviewed and saved.

## 8. Create a new migration

```powershell
# Create a migration after changing a SQLAlchemy database model.
.\.venv\Scripts\python.exe -m alembic revision --autogenerate -m "describe database change"
```

Important:

1. Read the created file in `backend\migrations\versions`.
2. Confirm that `upgrade()` and `downgrade()` are correct.
3. Only then run `alembic upgrade head`.

## 9. Validate a lesson batch JSON file

```powershell
# Validate JSON syntax without importing or changing the database.
.\.venv\Scripts\python.exe -m json.tool data\batches\BATCH-NAME.json | Out-Null

# Show success only when the JSON is valid.
if ($LASTEXITCODE -eq 0) {
    Write-Host "JSON valid."
}
```

Replace `BATCH-NAME.json` with the real file name.

Example:

```powershell
# Validate the German A1 batch.
.\.venv\Scripts\python.exe -m json.tool data\batches\de-a1-batch-02.json | Out-Null

# Show success only after valid JSON.
if ($LASTEXITCODE -eq 0) {
    Write-Host "JSON valid."
}
```

## 10. Import a lesson batch

```powershell
# Import only lesson codes that do not already exist in SQLite.
.\.venv\Scripts\python.exe scripts\import_lessons.py --file data\batches\BATCH-NAME.json
```

Example:

```powershell
# Import the English A2 lesson batch.
.\.venv\Scripts\python.exe scripts\import_lessons.py --file data\batches\en-a2-batch-02.json
```

Expected result:

```text
Imported file: BATCH-NAME.json
Created lessons: 10
Skipped lessons: 0
```

`Skipped lessons` means a lesson code already exists. It is not an error.

## 11. List local database files

```powershell
# Show database files in the project root.
Get-ChildItem -LiteralPath . -File -Filter "*.db" |
  Select-Object Name, Length, LastWriteTime
```

```powershell
# Show database files inside the active data folder.
Get-ChildItem -LiteralPath .\data -File -Filter "*.db" |
  Select-Object Name, Length, LastWriteTime
```

The active database must be:

```text
data\bridgeday.db
```

## 12. Check database tables with Python

```powershell
# Show all table names in the active SQLite database.
.\.venv\Scripts\python.exe -c "from sqlalchemy import inspect; from backend.app.database import engine; print(inspect(engine).get_table_names())"
```

## 13. Check the database in Beekeeper Studio

Open this file:

```text
C:\Users\user\Downloads\Bridgeday_language_lab\data\bridgeday.db
```

Useful SQL:

```sql
-- Show the migration currently saved in SQLite.
SELECT version_num AS current_migration
FROM alembic_version;
```

```sql
-- Show all columns in the lesson progress table.
PRAGMA table_info(lesson_progress);
```

```sql
-- Show users and their language profiles.
SELECT
    users.id,
    users.email,
    users.is_active,
    users.created_at,
    user_language_profiles.language_code,
    user_language_profiles.level_code
FROM users
JOIN user_language_profiles
    ON user_language_profiles.user_id = users.id
ORDER BY users.id, user_language_profiles.language_code;
```

## 14. Check Git changes

```powershell
# Show changed, deleted, and untracked project files.
git status --short
```

```powershell
# Show the current Git branch.
git branch --show-current
```

```powershell
# Show recent commits.
git log -10 --oneline
```

## 15. Check that Git does not track databases

```powershell
# List SQLite database files tracked by Git.
git ls-files "*.db"
```

The expected result is empty.

```powershell
# Show which ignore rule excludes the active database.
git check-ignore -v data\bridgeday.db
```

Expected result includes:

```text
.gitignore:*.db
```

## 16. Save a normal project change in Git

```powershell
# Review changed files before staging anything.
git status --short
```

```powershell
# Stage only the files that belong to the change.
git add PATH-TO-FILE
```

```powershell
# Create a commit with a clear message.
git commit -m "describe the change"
```

```powershell
# Send committed changes to GitHub.
git push
```

Do not use `git add .` until `git status --short` has been reviewed.

## 17. Test the mobile layout

1. Open `http://localhost:5500`.
2. Press `F12`.
3. Press `Ctrl + Shift + M`.
4. Test widths such as `320 × 750` and `375 × 812`.
5. Confirm that:
   - Home, Study, Review, and Progress are visible;
   - English and Deutsch buttons fit;
   - cards stay inside the screen;
   - no horizontal page scroll appears;
   - buttons remain clickable.

## 18. Ignore harmless browser messages

This message is normal and does not break BridgeDay:

```text
GET /.well-known/appspecific/com.chrome.devtools.json 404 Not Found
```

Chrome requests an optional DevTools file that BridgeDay does not use.

## 19. Useful recovery checks

```powershell
# Confirm the active database file exists.
Get-Item -LiteralPath .\data\bridgeday.db
```

```powershell
# Confirm front-end files exist.
Get-ChildItem -LiteralPath .\front -File |
  Select-Object Name
```

```powershell
# Confirm backend files exist.
Get-ChildItem -LiteralPath .\backend -Recurse -File |
  Select-Object FullName
```

## Safety rules

- Do not delete `data\bridgeday.db`.
- Do not commit `.env`.
- Do not commit `.db`, `.db-wal`, or `.db-shm` files.
- Validate JSON before importing lesson batches.
- Review generated migrations before applying them.
- Check `git status --short` before every commit.
- Keep front-end and back-end terminals open while using the full MVP.