README.txt

ToDo Full-Stack Application
==========================

OVERVIEW
--------
This is a full-stack ToDo application built using FastAPI for the backend
and React (Vite) for the frontend. The backend exposes REST APIs to manage
tasks, and the frontend consumes these APIs.

TECH STACK
----------
Backend  : FastAPI (Python)
Frontend : React (Vite)
Database : SQLite
Testing  : Pytest

PROJECT STRUCTURE
-----------------
ToDo/
├── app/                Backend (FastAPI)
├── tests/              Backend tests
├── frontend/           Frontend (React)
├── requirements.txt
├── todo.db
└── README.txt

SETUP INSTRUCTIONS
------------------

BACKEND SETUP
1. Create virtual environment:
   python -m venv virtualenv

2. Activate virtual environment (Windows):
   .\virtualenv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run backend:
   uvicorn app.main:app --reload

Backend URL:
http://127.0.0.1:8000

Swagger Docs:
http://127.0.0.1:8000/docs

FRONTEND SETUP
1. Navigate to frontend folder:
   cd frontend

2. Install dependencies:
   npm install

3. Run frontend:
   npm run dev

Frontend URL:
http://localhost:5173

CORS
----
CORS is enabled in the backend to allow requests from:
http://localhost:5173

TESTING
-------
Run tests using:
pytest -v

- Uses a separate test database
- Production database is not affected


AUTHOR
------
Rajat Agarwal
Python | FastAPI | React
