
from datetime import date

import pytest

from src import create_app
from src.api.model import Resort, WeatherForecast
from src.services.database import db


@pytest.fixture
def client(tmp_path):
    # Create an isolated SQLite database for testing
    test_database = tmp_path / "test.db"

    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{test_database}"
    })

    with app.app_context():
        db.create_all()

        resort = Resort(
            name="Test Mountain",
            location="Idaho"
        )

        db.session.add(resort)
        db.session.flush()

        resort_id = resort.id

        db.session.add_all([
            WeatherForecast(
                resort_id=resort_id,
                forecast_date=date(2026, 11, 20),
                temperature=20.0,
                description="Snow"
            ),
            WeatherForecast(
                resort_id=resort_id,
                forecast_date=date(2026, 11, 21),
                temperature=40.0,
                description="Cloudy"
            )
        ])

        db.session.commit()

        with app.test_client() as test_client:
            yield test_client

        db.session.remove()
        db.drop_all()


def test_get_resorts(client):
    response = client.get("/api/resorts")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data["resorts"]) == 1
    assert data["resorts"][0]["name"] == "Test Mountain"


def test_average_temperature_endpoint(client):
    response = client.get(
        "/api/resorts/1/average-temperature"
        "?start_date=2026-11-20&end_date=2026-11-21"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["average_temperature"] == 30.0
    assert data["forecast_count"] == 2


def test_average_temperature_invalid_dates(client):
    response = client.get(
        "/api/resorts/1/average-temperature"
        "?start_date=2026-11-22&end_date=2026-11-20"
    )

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_resort_not_found(client):
    response = client.get("/api/resorts/999")

    assert response.status_code == 404
