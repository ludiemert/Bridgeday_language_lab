from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from ..core.security import (
    create_access_token,
    hash_password,
    read_access_token,
    verify_password,
)
from ..database import get_db
from ..models import User, UserLanguageProfile
from ..schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)

# Create the login routes.
router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)

# Read the Bearer token.
bearer_scheme = HTTPBearer(auto_error=False)


def build_user_response(user: User) -> UserResponse:
    # Read the user language levels.
    levels = {
        profile.language_code: profile.level_code for profile in user.language_profiles
    }

    # Send safe user data.
    return UserResponse(
        id=user.id,
        email=user.email,
        english_level=levels.get("en", ""),
        german_level=levels.get("de", ""),
    )


@router.post(
    "/register",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    data: RegisterRequest,
    database: Session = Depends(get_db),
) -> TokenResponse:
    # Check if the email exists.
    user_exists = database.scalar(
        select(User).where(User.email == data.email),
    )

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists.",
        )

    # Create the new user.
    user = User(
        email=data.email,
        password_hash=hash_password(data.password),
        language_profiles=[
            UserLanguageProfile(
                language_code="en",
                level_code=data.english_level,
            ),
            UserLanguageProfile(
                language_code="de",
                level_code=data.german_level,
            ),
        ],
    )

    # Save the user in the database.
    database.add(user)
    database.commit()
    database.refresh(user)

    # Create the login token.
    token = create_access_token(user.id)

    return TokenResponse(
        access_token=token,
        token_type="bearer",
        user=build_user_response(user),
    )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login_user(
    data: LoginRequest,
    database: Session = Depends(get_db),
) -> TokenResponse:
    # Find the user and profiles.
    user = database.scalar(
        select(User)
        .options(selectinload(User.language_profiles))
        .where(User.email == data.email),
    )

    # Check the email and password.
    if not user or not verify_password(
        data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong email or password.",
        )

    # Check if the user is active.
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is not active.",
        )

    # Create the login token.
    token = create_access_token(user.id)

    return TokenResponse(
        access_token=token,
        token_type="bearer",
        user=build_user_response(user),
    )


@router.get(
    "/me",
    response_model=UserResponse,
)
def read_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(
        bearer_scheme,
    ),
    database: Session = Depends(get_db),
) -> UserResponse:
    # Check if the token exists.
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login is required.",
        )

    # Read the user ID from the token.
    user_id = read_access_token(credentials.credentials)

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token.",
        )

    # Find the current user.
    user = database.scalar(
        select(User)
        .options(selectinload(User.language_profiles))
        .where(User.id == user_id),
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User was not found.",
        )

    return build_user_response(user)
