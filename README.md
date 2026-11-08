
# Ski Resort Conditions Finder

A Python-based web application designed to help skiers and snowboarders compare weather and snow conditions at ski resorts throughout Idaho.

## Project Overview

Skiers and snowboarders often have to visit multiple resort websites to compare snowfall, temperatures, and weather forecasts before deciding where to ski. The Ski Resort Conditions Finder aims to simplify this process by automatically collecting weather data from external sources and displaying it in one location.

The application will allow users to compare Idaho ski resorts, view weather forecasts, and identify which mountains may have the best conditions for their next trip.

## Planned Features

- **Resort Selection:** View and select ski resorts throughout Idaho.
- **Weather Data Collection:** Automatically retrieve weather forecasts from an external API.
- **Resort Comparison:** Compare predicted snowfall and temperatures across multiple resorts.
- **Resort Rankings:** Rank resorts based on selected weather conditions.
- **Historical Data:** Store previously collected weather information to track changes over time.
- **Web Dashboard:** Display resort conditions and comparisons through a simple interface.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| Frontend | HTML, CSS |
| REST API | Flask routes |
| Weather Data | Open-Meteo API (planned) |
| Database | SQLite (planned) |
| Testing | pytest (planned) |
| Message Queue | RabbitMQ (planned) |
| CI/CD | GitHub Actions (planned) |
| Deployment | To be determined |

## Project Structure

The initial project structure is:

```text
ski-resort-conditions-finder/
├── src/
│   └── app.py
├── .gitignore
├── requirements.txt
└── README.md
```

Additional modules for data collection, analysis, database models, and testing will be added as development progresses.

## Getting Started

### Prerequisites

- Python 3
- pip
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/nyahnelson/ski-resort-conditions-finder.git
cd ski-resort-conditions-finder
```

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

Start the Flask development server:

```bash
flask --app src/app run
```

Open the application in your browser:

http://127.0.0.1:5000/

## Development Roadmap

### Phase 1: Web Application and Repository Setup
- Create the Flask application.
- Implement a basic HTML form for selecting ski resorts.
- Set up the GitHub repository.
- Deploy a publicly accessible website.

### Phase 2: Data Collection and Persistence
- Integrate an external weather API.
- Collect weather forecasts for supported Idaho ski resorts.
- Store collected information in a database.

### Phase 3: Data Analysis and Testing
- Implement snowfall and temperature comparisons.
- Rank resorts based on weather conditions.
- Add unit and integration tests.

### Phase 4: Advanced Features
- Implement event-based messaging with RabbitMQ.
- Configure continuous integration and delivery.
- Add application monitoring.

## Project Status

**In Development**

The project is currently in its initial setup phase. The first milestone is establishing a working Flask web application and hosting the source code on GitHub.
