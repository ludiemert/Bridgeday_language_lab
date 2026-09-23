# This file defines writing API request and response data.

# Import the data model tools.
from pydantic import BaseModel, Field


class SaveWritingRequest(BaseModel):
    # Read the lesson where the user wrote a sentence.
    lesson_code: str = Field(
        min_length=1,
        max_length=100,
    )

    # Read the learner sentence.
    text: str = Field(
        min_length=1,
        max_length=1000,
    )


class WritingEntryResponse(BaseModel):
    # Send the saved lesson code.
    lesson_code: str

    # Send the language of the real lesson track.
    language_code: str

    # Send the saved learner sentence.
    text: str
