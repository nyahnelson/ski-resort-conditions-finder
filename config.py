
import os

class Config:
    DEBUG = False
    TESTING = False

    WEATHER_API_URL = os.getenv(
        "WEATHER_API_URL",
        "https://api.open-meteo.com/v1/forecast"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///ski_conditions.db"
    )
