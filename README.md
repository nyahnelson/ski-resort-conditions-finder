
# Ski Resort Conditions Finder

A Python Flask web application that helps skiers and snowboarders view weather forecasts at ski resorts throughout Idaho.

## Project Overview

This application collects weather forecasts from the National Weather Service (NWS) API, stores them in a SQLite database, and displays resort conditions through a web interface.

**Supported Resorts:**
- Bogus Basin
- Brundage Mountain
- Tamarack Resort
- Sun Valley Resort

## Features

**Implemented:**
- Flask web application with resort selection and weather forecasts
- REST API endpoints for resort information
- Average-temperature calculator with date range selection
- Weather collection from the NWS API
- SQLite database with Flask-Migrate migrations
- Unit and integration tests using pytest
- Mock objects and spies for external API testing
- Continuous integration using GitHub Actions
- Cloud deployment using Render
- Production health checks and Prometheus metrics

**Planned:**
- RabbitMQ event messaging
- Automated daily weather collection
- Resort comparisons and rankings
- Historical weather visualization

## Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.11 |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Weather API | National Weather Service |
| Database | SQLite, Flask-SQLAlchemy |
| Migrations | Flask-Migrate, Alembic |
| Testing | pytest, unittest.mock |
| CI/CD | GitHub Actions, Render |
| Monitoring | Prometheus Flask Exporter |

## Project Structure

```text
ski-resort-conditions-finder/
├── .github/workflows/
│   └── tests.yml
├── src/
│   ├── app.py
│   ├── api/
│   │   ├── router.py
│   │   ├── controller.py
│   │   └── model.py
│   ├── services/
│   │   ├── collector.py
│   │   ├── analyzer.py
│   │   └── database.py
│   ├── templates/
│   └── static/
├── tests/
├── migrations/
├── run_collector.py
├── requirements.txt
└── README.md
```

## Getting Started

Clone the repository and install dependencies:

```bash
git clone https://github.com/nyahnelson/ski-resort-conditions-finder.git
cd ski-resort-conditions-finder
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Initialize the database:

```bash
flask --app src.app db upgrade
```

Collect weather forecasts:

```bash
python run_collector.py
```

Start the application:

```bash
flask --app src.app run --debug
```

Visit http://127.0.0.1:5000/

## REST API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/resorts` | List all resorts |
| GET | `/api/resorts/<id>` | Get resort details |
| GET | `/api/resorts/<id>/average-temperature` | Calculate average temperature |
| GET | `/health` | Check database connectivity |
| GET | `/metrics` | View Prometheus metrics |

The average-temperature endpoint requires `start_date` and `end_date` query parameters in `YYYY-MM-DD` format.

## Testing

The application uses pytest for unit, integration, API, collector, and monitoring tests. Temporary databases and mocked NWS responses keep tests independent of production data and external services.

Run all tests:

```bash
python -m pytest tests/ -v
```

GitHub Actions automatically runs the test suite on pushes and pull requests to `main`.

## Deployment and Monitoring

The application is deployed on Render using Gunicorn.

```bash
gunicorn src.app:app
```

Monitoring includes:
- `/health` for database connectivity checks
- `/metrics` for HTTP request counts, response times, and statuses
- Render application logs

For local metrics testing with Flask debug mode:

```bash
DEBUG_METRICS=1 flask --app src.app run --debug
```

Continuous delivery is being configured so Render deploys changes after GitHub Actions tests pass.

## Development Roadmap

**Level C — Complete**
- [x] Web application, data collection, and analysis
- [x] Database persistence and REST API
- [x] Unit testing and cloud deployment

**Level B — Implemented**
- [x] Integration tests
- [x] Mock objects and spies
- [x] Continuous integration
- [x] Production monitoring

**Level A — In Progress**
- [ ] RabbitMQ event collaboration
- [ ] Verify continuous delivery after successful CI

## Project Status

**Level B Implemented — Working Toward Level A**

The application is deployed on Render with automated testing, REST APIs, weather analysis, and production monitoring. Remaining work focuses on RabbitMQ messaging and verifying continuous delivery.
