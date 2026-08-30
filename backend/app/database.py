from collections.abc import Generator
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

# Find the project folder.
PROJECT_DIR = Path(__file__).resolve().parents[2]

# Create the data folder if needed.
DATA_DIR = PROJECT_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Set the SQLite database file.
DATABASE_FILE = DATA_DIR / "bridgeday.db"
DATABASE_URL = f"sqlite:///{DATABASE_FILE.as_posix()}"

# Create the database engine.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Create database sessions.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# Create the base class for tables.
class Base(DeclarativeBase):
    pass


# Give one database session to each request.
def get_db() -> Generator[Session, None, None]:
    # Open the database session.
    database = SessionLocal()

    try:
        # Send the session to the API route.
        yield database
    finally:
        # Close the database session.
        database.close()
