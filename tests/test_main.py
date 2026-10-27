from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_contains_project_info() -> None:
    response = client.get("/")

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Cloud Run Showcase API"
    assert body["info"]["repository_url"].endswith("cloud-run-showcase")


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
