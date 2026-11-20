
from unittest.mock import patch

import pytest
from sqlalchemy.exc import OperationalError

from src import create_app
from src.services.database import db


@pytest.fixture
def client(tmp_path):
    test_database = tmp_path / "monitoring.db"

    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{test_database}"
    })

    with app.app_context():
        db.create_all()

        with app.test_client() as test_client:
            yield test_client

        db.session.remove()
        db.drop_all()


def test_health_check_success(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
    assert response.get_json()["database"] == "connected"


def test_health_check_database_failure(client):
    with patch(
        "src.api.router.db.session.execute",
        side_effect=OperationalError(
            "SELECT 1", {}, Exception("Database unavailable")
        )
    ):
        response = client.get("/health")

    assert response.status_code == 503
    assert response.get_json()["status"] == "unhealthy"
    assert response.get_json()["database"] == "disconnected"


def test_prometheus_metrics_endpoint(client):
    # Generate a request so Prometheus has something to record
    client.get("/health")

    response = client.get("/metrics")

    assert response.status_code == 200
    assert b"flask_http_request" in response.data
