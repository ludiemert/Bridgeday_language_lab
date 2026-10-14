---

# Documentation and Git Workflow

## Internal documentation

Project documentation is inside the `info` folder:

- [Project status](PROJECT_STATUS.md)
- [Commands guide](COMMANDS.md)
- [Learning guide](LEARNING_GUIDE.md)
- [Development history](NOTES_HISTORY.md)

## Documentation commit

Before committing, check that `NOTES_HISTORY.md` does not contain a real password, token, or `SECRET_KEY` value.

```powershell
# Review changed and new files before staging.
git status --short
```

```powershell
# Stage the README and internal documentation files.
git add `
  README.md `
  info/PROJECT_STATUS.md `
  info/COMMANDS.md `
  info/LEARNING_GUIDE.md `
  info/NOTES_HISTORY.md
```

```powershell
# Review exactly what will enter the commit.
git diff --cached
```

```powershell
# Save the documentation update in local Git history.
git commit -m "organize project documentation"
```

```powershell
# Send the committed documentation to GitHub.
git push origin main
```

## Standard Git workflow

Use this process whenever you start new work.

### Before starting work

```powershell
# Check whether the local project has unfinished changes.
git status --short
```

If the result is empty, update the local project:

```powershell
# Download the latest main branch history without creating a merge commit.
git pull --rebase origin main
```

### After making changes

```powershell
# Review every changed, deleted, and new file.
git status --short
```

```powershell
# Stage all expected project changes.
# Only use this after checking git status carefully.
git add .
```

```powershell
# Review the exact staged changes before committing.
git diff --cached
```

```powershell
# Save a local version with a clear description.
git commit -m "describe the change"
```

```powershell
# Send the local commit to the main branch on GitHub.
git push origin main
```

## Git command summary

| Command | What it does |
| --- | --- |
| `git status` | Shows the current project state |
| `git pull --rebase origin main` | Updates the local project from GitHub |
| `git add .` | Stages expected changed files |
| `git diff --cached` | Shows what will be committed |
| `git commit -m "message"` | Saves a local project version |
| `git push origin main` | Sends commits to GitHub |

## Important Git safety rule

Never run `git add .` before reading `git status --short`.

This protects the project from accidentally committing:

- private files;
- `.env` files;
- database files;
- temporary files;
- unrelated edits.