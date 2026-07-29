# Task API with SQLite

A simple CRUD API built with FastAPI and SQLite.

## Why SQLite?

SQLite was chosen because:

- It requires no separate database server
- It is lightweight and easy to set up
- The entire database is stored in a single file
- It is perfect for small projects and learning backend development

## Database Location

The SQLite database is stored as:

```text
tasks.db
```

inside the project root directory.

The database and table are automatically created when the application starts.

## Project Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd FlyRank-Week3
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

### 5. Start the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Automatic Database Creation

When the application starts:

- `tasks.db` is created automatically if it does not exist
- The `tasks` table is created automatically
- Example tasks are inserted only when the table is empty

## Example SQL Query

The following query was executed during Stage 4:

```sql
SELECT * FROM tasks WHERE done = 1;
```

This returns all completed tasks.

## Database Viewer Screenshot

Insert a screenshot of DB Browser for SQLite here.

Example:

![SQLite Viewer](images/sqlite-viewer.png)

## Features

- Create tasks
- Read tasks
- Update tasks
- Delete tasks
- Persistent storage using SQLite
- Automatic database initialization



## Data Persistence Verification

The application uses a named Docker volume (`postgres_data`) for PostgreSQL storage.

### Test Procedure

1. Started the application:

```bash
docker compose up --build
```

2. Created a new task:

```bash
curl -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Persistence Test"}'
```

Response:

```json
{"id":4,"title":"Persistence Test","done":false}
```

3. Stopped the containers:

```bash
docker compose down
```

4. Restarted the containers:

```bash
docker compose up --build
```

5. Retrieved all tasks:

```bash
curl http://localhost:8000/tasks
```

Result:

```json
[
  {"id":1,"title":"Learn FastAPI","done":false},
  {"id":2,"title":"Build CRUD API","done":true},
  {"id":3,"title":"Connect PostgreSQL","done":false},
  {"id":4,"title":"Persistence Test","done":false}
]
```

The task created before the restart remained in the database after the containers were recreated, confirming that PostgreSQL data persistence is working through the Docker volume.

## Repository Update

The original repository was replaced with a clean FastAPI CRUD implementation using PostgreSQL and Docker.

Key updates include:

* FastAPI REST API implementation.
* PostgreSQL database running in Docker.
* Docker Compose orchestration for application and database services.
* Automatic database initialization and seed data.
* Database connection retry logic to handle container startup order.
* Persistent PostgreSQL storage using a named Docker volume.
* Environment-variable-based configuration using `.env`.
