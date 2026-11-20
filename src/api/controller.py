
from src.api.model import Resort
from src.services.database import db
from src.api.model import WeatherForecast
from src.services.analyzer import calculate_average_temperature

def get_all_resorts():
    resorts = db.session.execute(
        db.select(Resort).order_by(Resort.id)
    ).scalars().all()

    return [resort.to_dict() for resort in resorts]


def get_resort_by_id(resort_id):
    resort = db.session.get(Resort, resort_id)

    if resort is None:
        return None

    return resort.to_dict()

from datetime import timedelta
from sqlalchemy import func

def get_forecasts_by_resort(resort_id):
    # Find the latest collection timestamp for this resort
    latest_collection = db.session.execute(
        db.select(func.max(WeatherForecast.collected_at))
        .where(WeatherForecast.resort_id == resort_id)
    ).scalar_one_or_none()

    if latest_collection is None:
        return []

    # Forecasts in one run have slightly different timestamps.
    # Use a 10-minute window to identify the latest collection.
    collection_start = latest_collection - timedelta(minutes=10)

    forecasts = db.session.execute(
        db.select(WeatherForecast)
        .where(
            WeatherForecast.resort_id == resort_id,
            WeatherForecast.collected_at >= collection_start,
            WeatherForecast.collected_at <= latest_collection
        )
        .order_by(
            WeatherForecast.forecast_date,
            WeatherForecast.id
        )
    ).scalars().all()

    return [forecast.to_dict() for forecast in forecasts]

def get_average_temperature(resort_id, start_date, end_date):
    result = calculate_average_temperature(
        resort_id,
        start_date,
        end_date
    )

    return {
        "resort_id": resort_id,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        **result
    }