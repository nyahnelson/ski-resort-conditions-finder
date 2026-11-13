
from datetime import datetime, timezone
from src.services.database import db


class Resort(db.Model):
    __tablename__ = "resorts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    forecasts = db.relationship(
        "WeatherForecast",
        back_populates="resort"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location
        }


class WeatherForecast(db.Model):
    __tablename__ = "weather_forecasts"

    id = db.Column(db.Integer, primary_key=True)

    resort_id = db.Column(
        db.Integer,
        db.ForeignKey("resorts.id"),
        nullable=False
    )

    forecast_date = db.Column(db.Date, nullable=False)
    temperature = db.Column(db.Float)
    snowfall = db.Column(db.Float)
    description = db.Column(db.String(255))

    collected_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        nullable=False
    )

    resort = db.relationship(
        "Resort",
        back_populates="forecasts"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "resort_id": self.resort_id,
            "forecast_date": self.forecast_date.isoformat(),
            "temperature": self.temperature,
            "snowfall": self.snowfall,
            "collected_at": self.collected_at.isoformat(),
            "description": self.description
        }
