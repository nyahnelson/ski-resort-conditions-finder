
from flask import Flask
from src.services.database import db, migrate


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///ski_conditions.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so migrations can detect the tables
    from src.api import model

    from src.api.router import api_bp
    app.register_blueprint(api_bp)

    return app
