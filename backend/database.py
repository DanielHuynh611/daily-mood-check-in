"""Small SQLite persistence boundary for Daily."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from flask import current_app, g


def connect_database(path: str) -> sqlite3.Connection:
    connection = sqlite3.connect(path, timeout=5)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA busy_timeout = 5000")
    if path != ":memory:":
        connection.execute("PRAGMA journal_mode = WAL")
    return connection


def get_database() -> sqlite3.Connection:
    if "database" not in g:
        g.database = connect_database(current_app.config["DATABASE_PATH"])
    return g.database


def close_database(_error: BaseException | None = None) -> None:
    connection = g.pop("database", None)
    if connection is not None:
        connection.close()


def initialise_database(app) -> None:
    database_path = app.config["DATABASE_PATH"]
    if database_path != ":memory:":
        Path(database_path).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)

    schema_path = Path(app.root_path).parent / "database" / "schema.sql"
    connection = connect_database(database_path)
    try:
        connection.executescript(schema_path.read_text(encoding="utf-8"))
        connection.commit()
    finally:
        connection.close()

    app.teardown_appcontext(close_database)
