from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    # Read the new user data.
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=72,
    )
    english_level: Literal["A1", "A2", "B1", "B2", "C1", "C2"]
    german_level: Literal["A1", "A2", "B1", "B2", "C1", "C2"]


class LoginRequest(BaseModel):
    # Read the login data.
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=72,
    )


class UserResponse(BaseModel):
    # Send safe user data.
    id: int
    email: EmailStr
    english_level: str
    german_level: str


class TokenResponse(BaseModel):
    # Send the login token.
    access_token: str
    token_type: str
    user: UserResponse
