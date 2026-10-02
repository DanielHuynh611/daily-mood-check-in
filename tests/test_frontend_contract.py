from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def test_template_has_five_accessible_mood_options():
    template = (PROJECT_ROOT / "frontend" / "templates" / "app.html").read_text()

    assert template.count('type="radio" name="mood"') == 5
    for label in ("Very happy", "Happy", "Neutral", "Sad", "Very sad"):
        assert f"<span>{label}</span>" in template


def test_note_limit_matches_the_browser_logic():
    template = (PROJECT_ROOT / "frontend" / "templates" / "app.html").read_text()
    javascript = (PROJECT_ROOT / "frontend" / "static" / "js" / "app.js").read_text()

    assert 'maxlength="200"' in template
    assert "const MAX_NOTE_LENGTH = 200" in javascript


def test_no_remote_frontend_dependencies_are_loaded():
    templates = [
        (PROJECT_ROOT / "frontend" / "templates" / "app.html").read_text(),
        (PROJECT_ROOT / "frontend" / "templates" / "auth.html").read_text(),
    ]

    for template in templates:
        assert "https://" not in template
        assert "http://" not in template


def test_frontend_uses_authenticated_api_not_browser_storage():
    javascript = (PROJECT_ROOT / "frontend" / "static" / "js" / "app.js").read_text()

    assert 'apiRequest("/api/entries"' in javascript
    assert "localStorage" not in javascript


def test_authentication_template_has_expected_fields_and_csrf():
    template = (PROJECT_ROOT / "frontend" / "templates" / "auth.html").read_text()

    assert 'name="email"' in template
    assert 'name="password"' in template
    assert 'name="confirm_password"' in template
    assert 'name="csrf_token"' in template
