from backend import create_app


def make_client():
    return create_app(testing=True).test_client()


def test_check_in_is_the_default_screen():
    response = make_client().get("/")

    assert response.status_code == 200
    assert b"How are you feeling?" in response.data
    assert b'data-page="check-in"' in response.data


def test_check_in_alias_renders_the_same_workflow():
    response = make_client().get("/check-in")

    assert response.status_code == 200
    assert b"Save today" in response.data


def test_history_screen_is_available():
    response = make_client().get("/history")

    assert response.status_code == 200
    assert b"Mood history" in response.data
    assert b'data-page="history"' in response.data


def test_health_endpoint_is_machine_readable():
    response = make_client().get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"service": "daily", "status": "ok"}


def test_security_headers_are_applied():
    response = make_client().get("/")

    assert "default-src 'self'" in response.headers["Content-Security-Policy"]
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert response.headers["Referrer-Policy"] == "no-referrer"


def test_frontend_assets_are_served():
    client = make_client()

    stylesheet = client.get("/static/css/app.css")
    javascript = client.get("/static/js/app.js")

    assert stylesheet.status_code == 200
    assert b"prefers-reduced-motion" in stylesheet.data
    assert javascript.status_code == 200
    assert b"daily.moodEntries.v1" in javascript.data
