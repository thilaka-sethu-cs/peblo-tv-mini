# Peblo TV Mini

## Project Overview

Peblo TV Mini is a full-stack application for managing TV shows, seasons, and episodes.

## Features

- Create, view, update, and delete shows
- Create, view, update, and delete seasons
- Create, view, update, and delete episodes
- View seasons belonging to a show
- View episodes belonging to a season
- Health check endpoint

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn

## API Documentation

The backend provides interactive API documentation through Swagger UI.

Run the application using:

```bash
uvicorn main:app --reload

Then open:

http://127.0.0.1:8000/docs

## API Endpoints

### Shows

- GET `/shows/`
- POST `/shows/`
- PUT `/shows/{show_id}`
- DELETE `/shows/{show_id}`
- GET `/shows/{show_id}/seasons`

### Seasons

- GET `/seasons/`
- POST `/seasons/`
- GET `/seasons/{season_id}`
- PUT `/seasons/{season_id}`
- DELETE `/seasons/{season_id}`
- GET `/seasons/{season_id}/episodes`

### Episodes

- GET `/episodes/`
- POST `/episodes/`
- GET `/episodes/{episode_id}`
- PUT `/episodes/{episode_id}`
- DELETE `/episodes/{episode_id}`

## API Relationships

Show
 └── Seasons
      └── Episodes

## CRUD Operations

The project demonstrates:

- GET – Retrieve data
- POST – Create data
- PUT – Update data
- DELETE – Delete data

## Health Check

The API provides a health-check endpoint:

`GET /health`

A successful response confirms that the API is running.

## Project Structure

peblo-tv-mini/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   └── database.py
│   ├── main.py
│   └── requirements.txt
│
├── alembic/
├── alembic.ini
├── .gitignore
└── README.md

## Author

Thilaka