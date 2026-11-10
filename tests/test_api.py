
import pytest
from src import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Idaho Ski Conditions Finder" in response.data

def test_get_resorts(client):
    response = client.get("/api/resorts")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data["resorts"]) == 4
    assert data["resorts"][0]["name"] == "Bogus Basin"

def test_get_resort_by_id(client):
    response = client.get("/api/resorts/1")

    assert response.status_code == 200
    assert response.get_json()["name"] == "Bogus Basin"

def test_resort_not_found(client):
    response = client.get("/api/resorts/999")

    assert response.status_code == 404


def test_conditions_form(client):
    response = client.get("/conditions?resort_id=1")

    assert response.status_code == 200
    assert b"Bogus Basin" in response.data

