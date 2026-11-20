
import os

from flask import Flask
from src.services.database import db, migrate
from prometheus_flask_exporter import PrometheusMetrics

def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL",
        "sqlite:///ski_conditions.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Apply test configuration BEFORE initializing the database
    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Enable Prometheus metrics for production monitoring
    metrics = PrometheusMetrics(app, path="/metrics")

    from src.api import model
    from src.api.router import api_bp

    app.register_blueprint(api_bp)

    return app
