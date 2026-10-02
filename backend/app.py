"""Flask application for the Daily mood check-in."""

from __future__ import annotations

import os
import re
import secrets
import sqlite3
from datetime import UTC, date, datetime
from functools import wraps
from pathlib import Path
from uuid import uuid4

from flask import (
    Flask,
    flash,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.security import check_password_hash, generate_password_hash

from .database import get_database, initialise_database


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ALLOWED_MOODS = {"very_happy", "happy", "neutral", "sad", "very_sad"}
EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
MAX_NOTE_LENGTH = 200


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def env_flag(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def create_app(testing: bool = False, config: dict | None = None) -> Flask:
    """Create and configure the Daily web application."""

    app = Flask(
        __name__,
        template_folder=str(PROJECT_ROOT / "frontend" / "templates"),
        static_folder=str(PROJECT_ROOT / "frontend" / "static"),
        static_url_path="/static",
    )
    environment = os.getenv("DAILY_ENV", "development").strip().lower()
    database_path = os.getenv(
        "DATABASE_PATH",
        str(PROJECT_ROOT / "instance" / "daily.db"),
    )
    secret_key = os.getenv("SECRET_KEY", "")
    if testing:
        secret_key = secret_key or "daily-test-secret"
    elif environment == "production" and not secret_key:
        raise RuntimeError("SECRET_KEY must be set when DAILY_ENV=production")
    else:
        secret_key = secret_key or "daily-development-secret-change-me"

    app.config.update(
        TESTING=bool(testing),
        DATABASE_PATH=database_path,
        MAX_CONTENT_LENGTH=16 * 1024,
        SECRET_KEY=secret_key,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=env_flag("SESSION_COOKIE_SECURE"),
    )
    if config:
        app.config.update(config)

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)
    initialise_database(app)

    @app.before_request
    def load_signed_in_user() -> None:
        user_id = session.get("user_id")
        g.user = None
        if user_id is not None:
            g.user = get_database().execute(
                "SELECT id, email, created_at FROM users WHERE id = ?",
                (user_id,),
            ).fetchone()
            if g.user is None:
                session.clear()

    @app.context_processor
    def provide_template_context():
        return {"csrf_token": get_csrf_token, "current_user": g.get("user")}

    @app.after_request
    def add_security_headers(response):
        response.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; "
            "base-uri 'self'; "
            "connect-src 'self'; "
            "form-action 'self'; "
            "frame-ancestors 'none'; "
            "img-src 'self' data:; "
            "object-src 'none'; "
            "script-src 'self'; "
            "style-src 'self'",
        )
        response.headers.setdefault("Referrer-Policy", "no-referrer")
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault(
            "Permissions-Policy",
            "camera=(), geolocation=(), microphone=()",
        )
        response.headers.setdefault("Cache-Control", "no-store")
        if request.is_secure:
            response.headers.setdefault(
                "Strict-Transport-Security",
                "max-age=31536000; includeSubDomains",
            )
        return response

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if g.user is not None:
            return redirect(url_for("check_in"))
        if request.method == "POST":
            csrf_error = form_csrf_error()
            if csrf_error:
                flash(csrf_error, "error")
                return render_template("auth.html", mode="register", title="Create account"), 400

            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")
            confirm_password = request.form.get("confirm_password", "")
            error = validate_registration(email, password, confirm_password)
            if error is None:
                database = get_database()
                try:
                    cursor = database.execute(
                        "INSERT INTO users (email, password_hash, created_at) VALUES (?, ?, ?)",
                        (email, generate_password_hash(password), utc_now()),
                    )
                    database.commit()
                except sqlite3.IntegrityError:
                    error = "An account already exists for that email address."
                else:
                    session.clear()
                    session["user_id"] = cursor.lastrowid
                    get_csrf_token()
                    return redirect(url_for("check_in"))

            flash(error, "error")
        return render_template("auth.html", mode="register", title="Create account")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if g.user is not None:
            return redirect(url_for("check_in"))
        if request.method == "POST":
            csrf_error = form_csrf_error()
            if csrf_error:
                flash(csrf_error, "error")
                return render_template("auth.html", mode="login", title="Log in"), 400

            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")
            user = get_database().execute(
                "SELECT id, email, password_hash FROM users WHERE email = ? COLLATE NOCASE",
                (email,),
            ).fetchone()
            if user is None or not check_password_hash(user["password_hash"], password):
                flash("Email or password is incorrect.", "error")
            else:
                session.clear()
                session["user_id"] = user["id"]
                get_csrf_token()
                return redirect(url_for("check_in"))
        return render_template("auth.html", mode="login", title="Log in")

    @app.post("/logout")
    @login_required
    def logout():
        csrf_error = form_csrf_error()
        if csrf_error:
            return csrf_error, 400
        session.clear()
        return redirect(url_for("login"))

    @app.get("/")
    @login_required
    def check_in():
        return render_template("app.html", page="check-in", title="Daily check-in")

    @app.get("/check-in")
    @login_required
    def check_in_alias():
        return check_in()

    @app.get("/history")
    @login_required
    def history():
        return render_template("app.html", page="history", title="Mood history")

    @app.get("/api/entries")
    @api_login_required
    def list_entries():
        rows = get_database().execute(
            """
            SELECT id, entry_date, mood, note, created_at
            FROM mood_entries
            WHERE user_id = ?
            ORDER BY entry_date DESC, created_at DESC
            """,
            (g.user["id"],),
        ).fetchall()
        return jsonify({"entries": [serialise_entry(row) for row in rows]})

    @app.post("/api/entries")
    @api_login_required
    @api_csrf_required
    def create_entry():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "A JSON request body is required."}), 400

        if not all(
            isinstance(payload.get(field, ""), str)
            for field in ("entryDate", "mood", "note")
        ):
            return jsonify({"error": "Check-in fields must contain text values."}), 400

        entry_date = payload.get("entryDate", "").strip()
        mood = payload.get("mood", "").strip()
        note = payload.get("note", "").strip()
        error = validate_entry(entry_date, mood, note)
        if error:
            return jsonify({"error": error}), 400

        entry_id = str(uuid4())
        created_at = utc_now()
        database = get_database()
        try:
            database.execute(
                """
                INSERT INTO mood_entries (id, user_id, entry_date, mood, note, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (entry_id, g.user["id"], entry_date, mood, note, created_at),
            )
            database.commit()
        except sqlite3.IntegrityError:
            return jsonify({"error": "You already saved a check-in for that day."}), 409

        return (
            jsonify(
                {
                    "entry": {
                        "id": entry_id,
                        "entryDate": entry_date,
                        "mood": mood,
                        "note": note,
                        "createdAt": created_at,
                    }
                }
            ),
            201,
        )

    @app.delete("/api/entries/<entry_id>")
    @api_login_required
    @api_csrf_required
    def delete_entry(entry_id: str):
        database = get_database()
        cursor = database.execute(
            "DELETE FROM mood_entries WHERE id = ? AND user_id = ?",
            (entry_id, g.user["id"]),
        )
        database.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Check-in not found."}), 404
        return "", 204

    @app.delete("/api/entries")
    @api_login_required
    @api_csrf_required
    def clear_entries():
        database = get_database()
        database.execute(
            "DELETE FROM mood_entries WHERE user_id = ?",
            (g.user["id"],),
        )
        database.commit()
        return "", 204

    @app.get("/health")
    def health():
        return jsonify({"service": "daily", "status": "ok"}), 200

    return app


def get_csrf_token() -> str:
    token = session.get("csrf_token")
    if not token:
        token = secrets.token_urlsafe(32)
        session["csrf_token"] = token
    return token


def form_csrf_error() -> str | None:
    supplied = request.form.get("csrf_token", "")
    expected = session.get("csrf_token", "")
    if not supplied or not expected or not secrets.compare_digest(supplied, expected):
        return "The form expired. Please try again."
    return None


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


def api_login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if g.user is None:
            return jsonify({"error": "Please log in to continue."}), 401
        return view(*args, **kwargs)

    return wrapped


def api_csrf_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        supplied = request.headers.get("X-CSRF-Token", "")
        expected = session.get("csrf_token", "")
        if not supplied or not expected or not secrets.compare_digest(supplied, expected):
            return jsonify({"error": "The request expired. Refresh the page and try again."}), 400
        return view(*args, **kwargs)

    return wrapped


def validate_registration(email: str, password: str, confirmation: str) -> str | None:
    if len(email) > 254 or not EMAIL_PATTERN.fullmatch(email):
        return "Enter a valid email address."
    if len(password) < 8:
        return "Use at least 8 characters for your password."
    if len(password) > 128:
        return "Use no more than 128 characters for your password."
    if password != confirmation:
        return "The passwords do not match."
    return None


def validate_entry(entry_date: str, mood: str, note: str) -> str | None:
    try:
        date.fromisoformat(entry_date)
    except ValueError:
        return "Choose a valid check-in date."
    if mood not in ALLOWED_MOODS:
        return "Choose one of the available moods."
    if len(note) > MAX_NOTE_LENGTH:
        return f"The note must be {MAX_NOTE_LENGTH} characters or fewer."
    return None


def serialise_entry(row: sqlite3.Row) -> dict:
    return {
        "id": row["id"],
        "entryDate": row["entry_date"],
        "mood": row["mood"],
        "note": row["note"],
        "createdAt": row["created_at"],
    }
