
from datetime import date
from unittest.mock import patch

from src.services.analyzer import calculate_average_temperature


def test_average_temperature():
    """Verify the average temperature is calculated correctly."""

    with patch("src.services.analyzer.db") as mock_db:
        mock_db.session.execute.return_value.one.return_value = (30.0, 3)

        result = calculate_average_temperature(
            resort_id=1,
            start_date=date(2026, 11, 20),
            end_date=date(2026, 11, 22)
        )

        assert result["average_temperature"] == 30.0
        assert result["forecast_count"] == 3


def test_average_temperature_no_forecasts():
    """Verify empty results are handled correctly."""

    with patch("src.services.analyzer.db") as mock_db:
        mock_db.session.execute.return_value.one.return_value = (None, 0)

        result = calculate_average_temperature(
            resort_id=1,
            start_date=date(2026, 12, 1),
            end_date=date(2026, 12, 7)
        )

        assert result["average_temperature"] is None
        assert result["forecast_count"] == 0


def test_average_temperature_rounding():
    """Verify averages are rounded to two decimal places."""

    with patch("src.services.analyzer.db") as mock_db:
        mock_db.session.execute.return_value.one.return_value = (27.214285, 14)

        result = calculate_average_temperature(
            resort_id=1,
            start_date=date(2026, 11, 20),
            end_date=date(2026, 11, 26)
        )

        assert result["average_temperature"] == 27.21
        assert result["forecast_count"] == 14
