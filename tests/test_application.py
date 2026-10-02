import sqlite3

import pytest
from sqlalchemy.dialects import mysql
from sqlalchemy.schema import CreateTable
from werkzeug.security import check_password_hash

from backend.database import mood_entries, users
from fullstack import create_app


@pytest.fixture
def app(tmp_path):
    database_path = tmp_path / "daily-test.db"
    return create_app(
        testing=True,
        config={
            "DATABASE_URL": f"sqlite+pysqlite:///{database_path}",
            "TEST_DATABASE_PATH": str(database_path),
            "SECRET_KEY": "test-secret",
        },
    )


@pytest.fixture
def client(app):
    return app.test_client()


def csrf_token(client) -> str:
    with client.session_transaction() as browser_session:
        return browser_session["csrf_token"]


def register(client, email="student@example.com", password="password123"):
    client.get("/register")
    return client.post(
        "/register",
        data={
            "csrf_token": csrf_token(client),
            "email": email,
            "password": password,
            "confirm_password": password,
        },
        follow_redirects=False,
    )


def logout(client):
    return client.post(
        "/logout",
        data={"csrf_token": csrf_token(client)},
        follow_redirects=False,
    )


def create_entry(client, entry_date="2026-10-02", mood="happy", note="A calm day"):
    return client.post(
        "/api/entries",
        json={"entryDate": entry_date, "mood": mood, "note": note},
        headers={"X-CSRF-Token": csrf_token(client)},
    )


def test_anonymous_visitors_are_sent_to_login(client):
    response = client.get("/")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/login")
    assert client.get("/api/entries").status_code == 401


def test_registration_hashes_password_and_opens_check_in(client, app):
    response = register(client)

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")
    page = client.get("/")
    assert page.status_code == 200
    assert b"How are you feeling?" in page.data
    assert b"student@example.com" in page.data

    connection = sqlite3.connect(app.config["TEST_DATABASE_PATH"])
    password_hash = connection.execute(
        "SELECT password_hash FROM users WHERE email = ?",
        ("student@example.com",),
    ).fetchone()[0]
    connection.close()
    assert password_hash != "password123"
    assert check_password_hash(password_hash, "password123")


def test_registration_validation_and_duplicate_email(client):
    client.get("/register")
    invalid = client.post(
        "/register",
        data={
            "csrf_token": csrf_token(client),
            "email": "not-an-email",
            "password": "short",
            "confirm_password": "different",
        },
    )
    assert invalid.status_code == 200
    assert b"Enter a valid email address" in invalid.data

    assert register(client).status_code == 302
    logout(client)
    duplicate = register(client, email="STUDENT@example.com")
    assert duplicate.status_code == 200
    assert b"already exists" in duplicate.data


def test_login_rejects_wrong_password_and_logout_ends_session(client):
    register(client)
    logout(client)
    client.get("/login")

    rejected = client.post(
        "/login",
        data={
            "csrf_token": csrf_token(client),
            "email": "student@example.com",
            "password": "wrong-password",
        },
    )
    assert b"Email or password is incorrect" in rejected.data

    accepted = client.post(
        "/login",
        data={
            "csrf_token": csrf_token(client),
            "email": "student@example.com",
            "password": "password123",
        },
        follow_redirects=False,
    )
    assert accepted.status_code == 302
    assert logout(client).status_code == 302
    assert client.get("/").headers["Location"].endswith("/login")


def test_check_in_and_history_screens_are_authenticated(client):
    register(client)

    check_in = client.get("/check-in")
    history = client.get("/history")
    assert check_in.status_code == 200
    assert b"Save today" in check_in.data
    assert b'data-page="check-in"' in check_in.data
    assert history.status_code == 200
    assert b"Mood history" in history.data
    assert b'data-page="history"' in history.data


def test_entry_is_persisted_and_duplicate_day_is_rejected(client):
    register(client)

    created = create_entry(client)
    assert created.status_code == 201
    assert created.get_json()["entry"]["note"] == "A calm day"

    duplicate = create_entry(client, mood="sad")
    assert duplicate.status_code == 409
    assert "already saved" in duplicate.get_json()["error"]

    entries = client.get("/api/entries").get_json()["entries"]
    assert len(entries) == 1
    assert entries[0]["mood"] == "happy"


def test_entry_survives_a_fresh_application_instance(client, app):
    register(client)
    create_entry(client)
    database_url = app.config["DATABASE_URL"]

    restarted_client = create_app(
        testing=True,
        config={"DATABASE_URL": database_url, "SECRET_KEY": "test-secret"},
    ).test_client()
    restarted_client.get("/login")
    restarted_client.post(
        "/login",
        data={
            "csrf_token": csrf_token(restarted_client),
            "email": "student@example.com",
            "password": "password123",
        },
    )

    entries = restarted_client.get("/api/entries").get_json()["entries"]
    assert len(entries) == 1
    assert entries[0]["note"] == "A calm day"


def test_entry_validation_and_csrf_protection(client):
    register(client)

    missing_csrf = client.post(
        "/api/entries",
        json={"entryDate": "2026-10-02", "mood": "happy", "note": ""},
    )
    assert missing_csrf.status_code == 400

    invalid = create_entry(client, entry_date="not-a-date", mood="unknown", note="x" * 201)
    assert invalid.status_code == 400
    assert "valid check-in date" in invalid.get_json()["error"]


def test_users_cannot_read_or_delete_each_others_entries(client):
    register(client, "first@example.com")
    first_entry = create_entry(client).get_json()["entry"]
    logout(client)

    register(client, "second@example.com")
    assert client.get("/api/entries").get_json() == {"entries": []}
    denied = client.delete(
        f"/api/entries/{first_entry['id']}",
        headers={"X-CSRF-Token": csrf_token(client)},
    )
    assert denied.status_code == 404

    logout(client)
    client.get("/login")
    client.post(
        "/login",
        data={
            "csrf_token": csrf_token(client),
            "email": "first@example.com",
            "password": "password123",
        },
    )
    assert len(client.get("/api/entries").get_json()["entries"]) == 1


def test_entry_and_history_deletion(client):
    register(client)
    first = create_entry(client, "2026-10-01").get_json()["entry"]
    create_entry(client, "2026-10-02")

    deleted = client.delete(
        f"/api/entries/{first['id']}",
        headers={"X-CSRF-Token": csrf_token(client)},
    )
    assert deleted.status_code == 204
    assert len(client.get("/api/entries").get_json()["entries"]) == 1

    cleared = client.delete(
        "/api/entries",
        headers={"X-CSRF-Token": csrf_token(client)},
    )
    assert cleared.status_code == 204
    assert client.get("/api/entries").get_json() == {"entries": []}


def test_health_endpoint_and_security_headers(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"service": "daily", "status": "ok"}
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert response.headers["Referrer-Policy"] == "no-referrer"
    assert response.headers["Cache-Control"] == "no-store"


def test_frontend_assets_are_served(client):
    stylesheet = client.get("/static/css/app.css")
    javascript = client.get("/static/js/app.js")

    assert stylesheet.status_code == 200
    assert b"prefers-reduced-motion" in stylesheet.data
    assert javascript.status_code == 200
    assert b"/api/entries" in javascript.data


def test_schema_compiles_for_mysql():
    users_ddl = str(CreateTable(users).compile(dialect=mysql.dialect()))
    entries_ddl = str(CreateTable(mood_entries).compile(dialect=mysql.dialect()))

    assert "BIGINT UNSIGNED" in users_ddl
    assert "AUTO_INCREMENT" in users_ddl
    assert "ENGINE=InnoDB" in users_ddl
    assert "COLLATE utf8mb4_unicode_ci" in users_ddl
    assert "CHAR(36)" in entries_ddl
    assert "FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE" in entries_ddl
    assert "UNIQUE (user_id, entry_date)" in entries_ddl
