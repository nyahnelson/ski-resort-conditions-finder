from sqlalchemy import func

from src.api.model import WeatherForecast
from src.services.database import db


def calculate_average_temperature(resort_id, start_date, end_date):
    result = db.session.execute(
        db.select(
            func.avg(WeatherForecast.temperature),
            func.count(WeatherForecast.temperature)
        )
        .where(
            WeatherForecast.resort_id == resort_id,
            WeatherForecast.forecast_date.between(
                start_date, end_date
            )
        )
    ).one()

    average, count = result

    return {
        "average_temperature": round(average, 2)
        if average is not None else None,
        "forecast_count": count
    }