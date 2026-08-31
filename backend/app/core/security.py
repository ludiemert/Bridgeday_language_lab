from datetime import datetime, timedelta, timezone

import bcrypt
from jose import JWTError, jwt

from .config import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY


def hash_password(password: str) -> str:
    # Create a safe password hash.
    password_bytes = password.encode("utf-8")
    password_hash = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt(),
    )
    return password_hash.decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    # Check the user password.
    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8"),
    )


def create_access_token(user_id: int) -> str:
    # Set the token end time.
    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
    )

    # Create the token data.
    token_data = {
        "sub": str(user_id),
        "exp": expires_at,
    }

    # Create the signed token.
    return jwt.encode(
        token_data,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def read_access_token(token: str) -> int | None:
    # Read the signed token.
    try:
        token_data = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        user_id = token_data.get("sub")

        if user_id is None:
            return None

        return int(user_id)
    except (JWTError, TypeError, ValueError):
        return None
