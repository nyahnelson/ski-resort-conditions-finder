
# Ski Resort Conditions Finder

A Python Flask web application that helps skiers and snowboarders compare weather conditions at ski resorts throughout Idaho.

## Project Overview

Skiers often need to visit multiple websites to compare resort conditions. This application simplifies the process by collecting weather forecasts from the National Weather Service (NWS) API and storing them in a SQLite database.

Currently supported resorts:
- Bogus Basin
- Brundage Mountain
- Tamarack Resort
- Sun Valley Resort

## Features

**Implemented:**
- Flask web application with resort selection
- REST API endpoints for resort information
- Weather data collection from the NWS API
- SQLite database for storing resorts and weather forecasts
- Database schema migrations using Flask-Migrate

**Planned:**
- Resort comparisons and rankings
- Snowfall analysis
- Historical weather visualization
- Automated data collection
- CI/CD and cloud deployment

## Technology Stack

| Component | Technology |
|---|---|
| Language | Python |
| Backend | Flask |
| Frontend | HTML, CSS |
| Weather API | National Weather Service |
| Database | SQLite, Flask-SQLAlchemy |
| Migrations | Flask-Migrate, Alembic |
| Testing | pytest (planned) |
| Deployment | Render (planned) |

## Project Structure

```text
ski-resort-conditions-finder/
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
├── migrations/
├── run_collector.py
├── requirements.txt
└── README.md
```

## Getting Started

### Installation

Clone the repository:

```bash
git clone https://github.com/nyahnelson/ski-resort-conditions-finder.git
cd ski-resort-conditions-finder
```

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Database Setup

Apply database migrations to create the SQLite tables:

```bash
flask --app src.app db upgrade
```

The database is stored at `instance/ski_conditions.db`.

### Collect Weather Data

Run the data collector:

```bash
python run_collector.py
```

The collector retrieves approximately seven days of daytime and nighttime forecasts for each resort, typically saving 56 records per run.

Each record contains a forecast date, temperature, weather description, and collection timestamp. Snowfall amounts are currently unavailable from the selected NWS forecast endpoint.

### View Saved Data

Open the SQLite database:

```bash
sqlite3 instance/ski_conditions.db
```

Run:

```sql
SELECT * FROM weather_forecasts LIMIT 10;
```

Exit using `.quit`.

### Run the Web Application

```bash
flask --app src.app run --debug
```

Open http://127.0.0.1:5000/ in your browser.

## Database and Persistence

The application uses two tables:

- `resorts`: Stores resort names and locations.
- `weather_forecasts`: Stores weather forecasts linked to resorts by `resort_id`.

Flask-SQLAlchemy manages database operations, while Flask-Migrate and Alembic track schema changes in the `migrations/` directory.

To generate and apply a new schema migration:

```bash
flask --app src.app db migrate -m "Describe change"
flask --app src.app db upgrade
```

## Development Roadmap

- [x] Set up Flask application and GitHub repository
- [x] Implement resort selection and API endpoints
- [x] Integrate external weather API
- [x] Store weather forecasts in SQLite
- [x] Implement database migrations
- [ ] Implement resort comparisons and rankings
- [ ] Add automated testing and CI/CD
- [ ] Deploy the application

## Project Status

**In Development — Data Collection and Persistence Implemented**

The application successfully retrieves weather forecasts from the National Weather Service API and saves them to SQLite. Future development will focus on analyzing conditions and comparing resorts.
