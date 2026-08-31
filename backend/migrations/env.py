from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from backend.app import models
from backend.app.database import Base, DATABASE_URL

# Get the Alembic settings.
config = context.config

# Set the database file path.
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Set the log settings.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Find all database tables.
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    # Run without a database connection.
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    # Create a database connection.
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        # Compare models with database tables.
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
