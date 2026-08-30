from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


# Check if the API is working.
@app.get("/api/health")
def read_health():
    # Send a simple message.
    return {
        "status": "ok",
        "app": "BridgeDay API",
    }
