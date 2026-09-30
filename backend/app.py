"""Flask application for the Daily mood check-in."""

from __future__ import annotations

from pathlib import Path

from flask import Flask, jsonify, render_template


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def create_app(testing: bool = False) -> Flask:
    """Create the Daily web application."""

    app = Flask(
        __name__,
        template_folder=str(PROJECT_ROOT / "frontend" / "templates"),
        static_folder=str(PROJECT_ROOT / "frontend" / "static"),
        static_url_path="/static",
    )
    app.config.update(
        TESTING=bool(testing),
        MAX_CONTENT_LENGTH=16 * 1024,
    )

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
        return response

    @app.get("/")
    def check_in():
        return render_template("app.html", page="check-in", title="Daily check-in")

    @app.get("/check-in")
    def check_in_alias():
        return check_in()

    @app.get("/history")
    def history():
        return render_template("app.html", page="history", title="Mood history")

    @app.get("/health")
    def health():
        return jsonify({"service": "daily", "status": "ok"}), 200

    return app
