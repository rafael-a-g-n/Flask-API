# Flask-API — Minimal REST demo

> A small, elegant Flask API demonstrating basic REST concepts, JSON error handling, and simple in-memory data management.

[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.x-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/status-experimental-yellow.svg)]


**Why this project?**
- Lightweight reference for building and testing REST endpoints with Flask.
- Demonstrates routing, request parsing, JSON responses, error handlers, and simple in-memory persistence.
- Great for learning API basics or for use in workshops / exercises.

**Skills & Concepts Leveraged**
- RESTful API design: endpoints, HTTP verbs, status codes
- JSON request parsing and responses
- Flask routing and error handling (`@app.route`, `@app.errorhandler`)
- In-memory data structures and simple CRUD operations
- Local development workflows with virtual environments
- Git: commits and basic push workflow


**Tech Stack**
- Python 3.11+
- Flask 3.x
- Git (for version control)


## Project Structure

- `server.py` — main Flask application and endpoints
- `__pycache__/` — Python cache files
- `.venv/` — optional virtual environment (if created locally)


## API Overview

All endpoints return JSON and standard HTTP status codes.

- GET `/` — Hello world message
- GET `/data` — summary message about the in-memory dataset
- GET `/count` — returns `{"data_count": <n>}`
- GET `/name_search?q=<name>` — search by first name (query param)
- POST `/person` — add a person (JSON body required). Returns `{"id": "<id>"}` on success.
- GET `/person/<uuid>` — fetch person by UUID
- DELETE `/person/<uuid>` — remove person by UUID

Special behavior:
- All unknown routes return JSON `{"message": "API not found"}` with HTTP 404.


## Quick Start — Run Locally

1. Install Python 3.11+ (if not already installed).

2. Create and activate a virtual environment (recommended):

```bash
# create venv
python -m venv .venv

# activate (Git Bash / WSL)
source .venv/Scripts/activate

# on Windows PowerShell
# .\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install flask
# or, if you prefer a requirements file, create one with: pip freeze > requirements.txt
```

4. Run the app (Flask CLI):

```bash
python -m flask --app server --debug run --port 8080
```

Alternative: run the module directly if you add an entrypoint. Using the Flask module is portable and recommended.


## Example Requests

Add a person (POST):

```bash
curl -i -X POST \
  -H 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
        }' \
  http://localhost:8080/person
```

- Expected success response: `200 OK` with body `{"id":"4e1e61b4-8a27-11ed-a1eb-0242ac120002"}`
- If the request body is missing or empty the API returns `422` and `{"message":"Invalid input parameter"}`.

Fetch a person (GET):

```bash
curl http://localhost:8080/person/11111111-589a-43b6-9a5d-d1601cf51111
```

Delete a person (DELETE):

```bash
curl -X DELETE http://localhost:8080/person/11111111-589a-43b6-9a5d-d1601cf51111
```

Unknown routes:

```bash
curl -i http://localhost:8080/this-route-does-not-exist
# => 404 with JSON {"message":"API not found"}
```


## Contributing
- Fork the repo, create a branch, make changes, and open a pull request.
- Keep changes small & focused. Write clear commit messages.


## Author
- Rafael (project owner in this workspace)


## License
This project is provided as-is for learning purposes. Feel free to adopt and adapt.