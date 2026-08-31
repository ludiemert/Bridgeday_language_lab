import os
from pathlib import Path

from dotenv import load_dotenv

# Find the project folder.
PROJECT_DIR = Path(__file__).resolve().parents[3]

# Load private settings.
load_dotenv(PROJECT_DIR / ".env")

# Read the secret key.
SECRET_KEY = os.getenv("SECRET_KEY")

# Stop when the secret key is missing.
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is missing.")

# Set the token settings.
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10080
