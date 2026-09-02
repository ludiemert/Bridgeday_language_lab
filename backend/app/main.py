from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from .api.auth import router as auth_router

from .database import engine

# Import the lesson routes.
from .api.lessons import router as lesson_router

# Create the API app.
app = FastAPI(
    title="BridgeDay API",
    version="0.1.0",
)

# Allow the local front app.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add the login routes.
app.include_router(auth_router)

# Add the lesson routes.
app.include_router(lesson_router)


# Check the API and database.
@app.get("/api/health")
def read_health():
    # Open a short database connection.
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    # Send the system status.
    return {
        "status": "ok",
        "app": "BridgeDay API",
        "database": "ok",
    }
