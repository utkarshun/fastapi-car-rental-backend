# FastAPI Car Rental API

Backend REST API for a car rental platform, built with FastAPI.

## Highlights

- User management and authentication-ready structure
- Car management endpoints
- Booking workflow endpoints
- Clear modular architecture (routes, models, schemas, core, db)

## Tech Stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy (project structure indicates ORM usage)
- SQLite database file: car_rental_db

## Project Structure

- app/main.py
- app/core/
- app/db/
- app/models/
- app/routes/
- app/schemas/
- app/utils/

## Getting Started

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Run the API server.

Example (Windows PowerShell):

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload

## API Endpoints

Authentication:

- POST /register
- POST /login

Cars:

- POST /cars
- GET /cars
- PUT /car/{car_id}
- DELETE /cars/{car_id}

Bookings:

- POST /book

Health:

- GET /

## API Docs

After server start:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Environment

If environment variables are used, add them in a .env file.

## Author

Utkarsh
