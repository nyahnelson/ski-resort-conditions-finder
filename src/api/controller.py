
from src.api.model import Resort
from src.services.database import db
from src.api.model import WeatherForecast

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

def get_forecasts_by_resort(resort_id):
    forecasts = db.session.execute(
        db.select(WeatherForecast)
        .filter_by(resort_id=resort_id)
        .order_by(WeatherForecast.forecast_date)
    ).scalars().all()

    return [forecast.to_dict() for forecast in forecasts]