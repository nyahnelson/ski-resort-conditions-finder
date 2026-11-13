
import requests

NWS_API_URL = "https://api.weather.gov"

HEADERS = {
    "User-Agent": "SkiResortConditionsFinder/1.0 (student project)",
    "Accept": "application/geo+json"
}

RESORT_COORDINATES = {
    "Bogus Basin": (43.76, -116.10),
    "Brundage Mountain": (45.00, -116.15),
    "Tamarack Resort": (44.67, -116.12),
    "Sun Valley Resort": (43.68, -114.41)
}

RESORT_LOCATIONS = {
    "Bogus Basin": "Boise, Idaho",
    "Brundage Mountain": "McCall, Idaho",
    "Tamarack Resort": "Donnelly, Idaho",
    "Sun Valley Resort": "Sun Valley, Idaho"
}


def collect_weather_data(resort_name):
    if resort_name not in RESORT_COORDINATES:
        raise ValueError(f"Unknown resort: {resort_name}")

    latitude, longitude = RESORT_COORDINATES[resort_name]

    # First request: find the forecast endpoint
    points_url = f"{NWS_API_URL}/points/{latitude},{longitude}"

    points_response = requests.get(
        points_url,
        headers=HEADERS,
        timeout=30
    )
    points_response.raise_for_status()

    forecast_url = points_response.json()["properties"]["forecast"]

    # Second request: retrieve forecast periods
    forecast_response = requests.get(
        forecast_url,
        headers=HEADERS,
        timeout=30
    )
    forecast_response.raise_for_status()

    periods = forecast_response.json()["properties"]["periods"]

    forecasts = []

    for period in periods:
        forecasts.append({
            "resort": resort_name,
            "date": period["startTime"][:10],
            "temperature": period["temperature"],
            "description": period["shortForecast"],
            "snowfall": None
        })

    return forecasts


def collect_all_weather_data():
    all_forecasts = []

    for resort_name in RESORT_COORDINATES:
        print(f"Collecting forecasts for {resort_name}...")
        forecasts = collect_weather_data(resort_name)
        all_forecasts.extend(forecasts)

    return all_forecasts
