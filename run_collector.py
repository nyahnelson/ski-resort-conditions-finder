
from datetime import date

from src import create_app
from src.api.model import Resort, WeatherForecast
from src.services.database import db
from src.services.collector import (
    collect_all_weather_data,
    RESORT_LOCATIONS
)


def save_weather_data():
    # Fetch all forecasts before writing to the database
    forecasts = collect_all_weather_data()

    for forecast in forecasts:
        resort_name = forecast["resort"]

        # Find an existing resort
        resort = db.session.execute(
            db.select(Resort).filter_by(name=resort_name)
        ).scalar_one_or_none()

        # Create the resort if it does not exist
        if resort is None:
            resort = Resort(
                name=resort_name,
                location=RESORT_LOCATIONS[resort_name]
            )

            db.session.add(resort)
            db.session.flush()

        # Create a new weather forecast record
        weather = WeatherForecast(
            resort_id=resort.id,
            forecast_date=date.fromisoformat(forecast["date"]),
            temperature=forecast["temperature"],
            snowfall=forecast["snowfall"],
            description=forecast["description"]
        )

        db.session.add(weather)

    db.session.commit()

    print(f"Saved {len(forecasts)} weather forecasts!")


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        try:
            save_weather_data()
        except Exception:
            db.session.rollback()
            raise
