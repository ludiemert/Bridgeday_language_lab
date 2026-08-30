from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class User(Base):
    # Set the database table name.
    __tablename__ = "users"

    # Create the user ID.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Save a unique user email.
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    # Save the protected password.
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Check if the user can use the app.
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # Save the user creation time.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Connect the user with language profiles.
    language_profiles: Mapped[list["UserLanguageProfile"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
