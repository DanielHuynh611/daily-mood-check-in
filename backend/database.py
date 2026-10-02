"""SQLAlchemy Core persistence definitions for Daily."""

from __future__ import annotations

from flask import current_app
from sqlalchemy import (
    CheckConstraint,
    CHAR,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    MetaData,
    String,
    Table,
    UniqueConstraint,
    create_engine,
)
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.engine import Engine


metadata = MetaData()
user_id_type = BIGINT(unsigned=True).with_variant(Integer, "sqlite")

users = Table(
    "users",
    metadata,
    Column("id", user_id_type, primary_key=True, autoincrement=True),
    Column("email", String(254), nullable=False, unique=True),
    Column("password_hash", String(255), nullable=False),
    Column("created_at", DateTime(), nullable=False),
    mysql_engine="InnoDB",
    mysql_charset="utf8mb4",
    mysql_collate="utf8mb4_unicode_ci",
)

mood_entries = Table(
    "mood_entries",
    metadata,
    Column("id", CHAR(36), primary_key=True),
    Column(
        "user_id",
        user_id_type,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("entry_date", Date(), nullable=False),
    Column("mood", String(20), nullable=False),
    Column("note", String(200), nullable=False, server_default=""),
    Column("created_at", DateTime(), nullable=False),
    UniqueConstraint("user_id", "entry_date", name="uq_mood_entries_user_date"),
    CheckConstraint(
        "mood IN ('very_happy', 'happy', 'neutral', 'sad', 'very_sad')",
        name="ck_mood_entries_mood",
    ),
    CheckConstraint(
        "CHAR_LENGTH(note) <= 200",
        name="ck_mood_entries_note_length",
    ).ddl_if(dialect="mysql"),
    mysql_engine="InnoDB",
    mysql_charset="utf8mb4",
    mysql_collate="utf8mb4_unicode_ci",
)

Index(
    "ix_mood_entries_user_created",
    mood_entries.c.user_id,
    mood_entries.c.created_at.desc(),
)


def get_database() -> Engine:
    return current_app.extensions["daily_database_engine"]


def initialise_database(app) -> None:
    engine = create_engine(
        app.config["DATABASE_URL"],
        pool_pre_ping=True,
        pool_recycle=1800,
    )
    metadata.create_all(engine)
    app.extensions["daily_database_engine"] = engine
