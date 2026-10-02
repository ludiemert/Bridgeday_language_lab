"""add review count to lesson progress

Revision ID: b883e40f21a4
Revises: 3b775a3d3c07
Create Date: 2026-10-02 18:39:09.524882
"""

# Import Alembic migration type helpers.
from typing import Sequence, Union

# Import Alembic database operations.
from alembic import op

# Import SQLAlchemy column definitions.
import sqlalchemy as sa

# Set the migration identifiers.
revision: str = "b883e40f21a4"
down_revision: Union[str, Sequence[str], None] = "3b775a3d3c07"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add the review counter with zero for existing lesson progress.
    op.add_column(
        "lesson_progress",
        sa.Column(
            "review_count",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
    )


def downgrade() -> None:
    # Remove the review counter when rolling back this migration.
    op.drop_column(
        "lesson_progress",
        "review_count",
    )
