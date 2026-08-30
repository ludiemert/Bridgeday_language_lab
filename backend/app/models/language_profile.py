from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class UserLanguageProfile(Base):
    # Set the database table name.
    __tablename__ = "user_language_profiles"

    # Keep one language only once for each user.
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "language_code",
            name="unique_user_language",
        ),
    )

    # Create the profile ID.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Connect this profile to one user.
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    # Save the language code.
    language_code: Mapped[str] = mapped_column(
        String(2),
        nullable=False,
    )

    # Save the selected language level.
    level_code: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    # Save the profile creation time.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Connect this profile with the user.
    user: Mapped["User"] = relationship(
        back_populates="language_profiles",
    )
