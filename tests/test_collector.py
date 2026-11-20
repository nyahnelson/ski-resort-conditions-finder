
from unittest.mock import Mock, patch

import pytest
import requests

from src.services.collector import collect_weather_data


@patch("src.services.collector.requests.get")
def test_collect_weather_data_success(mock_get):
    """Test successful weather collection without calling NWS."""

    # Mock the response from the NWS points endpoint
    points_response = Mock()
    points_response.json.return_value = {
        "properties": {
            "forecast": "https://api.weather.gov/gridpoints/BOI/100,100/forecast"
        }
    }

    # Mock the response containing weather forecasts
    forecast_response = Mock()
    forecast_response.json.return_value = {
        "properties": {
            "periods": [
                {
                    "startTime": "2026-11-20T06:00:00-07:00",
                    "temperature": 30,
                    "shortForecast": "Snow"
                },
                {
                    "startTime": "2026-11-21T06:00:00-07:00",
                    "temperature": 35,
                    "shortForecast": "Cloudy"
                }
            ]
        }
    }

    # Return the two fake responses in order
    mock_get.side_effect = [
        points_response,
        forecast_response
    ]

    result = collect_weather_data("Bogus Basin")

    assert len(result) == 2
    assert result[0]["resort"] == "Bogus Basin"
    assert result[0]["date"] == "2026-11-20"
    assert result[0]["temperature"] == 30
    assert result[0]["description"] == "Snow"
    assert result[0]["snowfall"] is None

    # Spy: verify the HTTP client was called twice
    assert mock_get.call_count == 2


@patch("src.services.collector.requests.get")
def test_collect_weather_data_api_failure(mock_get):
    """Test that HTTP failures are propagated."""

    mock_get.return_value.raise_for_status.side_effect = (
        requests.exceptions.HTTPError("NWS API unavailable")
    )

    with pytest.raises(requests.exceptions.HTTPError):
        collect_weather_data("Bogus Basin")

    assert mock_get.call_count == 1


@patch("src.services.collector.requests.get")
def test_collect_weather_data_timeout(mock_get):
    """Test that a network timeout is handled."""

    mock_get.side_effect = requests.exceptions.Timeout(
        "NWS request timed out"
    )

    with pytest.raises(requests.exceptions.Timeout):
        collect_weather_data("Bogus Basin")

    assert mock_get.call_count == 1


@patch("src.services.collector.requests.get")
def test_collect_weather_data_invalid_resort(mock_get):
    """Test that unsupported resorts are rejected."""

    with pytest.raises(ValueError):
        collect_weather_data("Unknown Mountain")

    # Invalid resorts should never trigger an API request
    mock_get.assert_not_called()
