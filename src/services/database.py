
"""
Database Service

Responsible for storing and retrieving
ski resort weather information.
"""


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def initialize_database():
    raise NotImplementedError(
        "Database initialization has not been implemented yet."
    )
