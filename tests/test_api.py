
import pytest

from src import create_app
from src.api.model import Resort
from src.services.database import db


@pytest.fixture
def client(tmp_path):
    # Create a temporary database for this test
    test_database = tmp_path / "test.db"

    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{test_database}"
    })

    with app.app_context():
        # Create the database tables
        db.create_all()

        # Add the four resorts used by the application
        resorts = [
            Resort(name="Bogus Basin", location="Boise, Idaho"),
            Resort(name="Brundage Mountain", location="McCall, Idaho"),
            Resort(name="Tamarack Resort", location="Donnelly, Idaho"),
            Resort(name="Sun Valley Resort", location="Sun Valley, Idaho")
        ]

        db.session.add_all(resorts)
        db.session.commit()

        # Create the Flask test client
        with app.test_client() as test_client:
            yield test_client

        # Clean up the temporary database
        db.session.remove()
        db.drop_all()


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
