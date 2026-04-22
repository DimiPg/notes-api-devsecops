from fastapi.testclient import TestClient
from app.main import app, notes_db

client = TestClient(app)


def setup_function():
    notes_db.clear()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_notes_empty():
    response = client.get("/notes")
    assert response.status_code == 200
    assert response.json() == {"notes": []}


def test_create_note():
    response = client.post(
        "/notes",
        json={"title": "First note", "content": "Learning DevSecOps"},
    )
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["title"] == "First note"
    assert body["content"] == "Learning DevSecOps"


def test_get_notes_after_create():
    client.post(
        "/notes",
        json={"title": "First note", "content": "Learning DevSecOps"},
    )

    response = client.get("/notes")
    assert response.status_code == 200
    body = response.json()
    assert len(body["notes"]) == 1
    assert body["notes"][0]["title"] == "First note"