# Task API with FastAPI, PostgreSQL, and Docker

A simple CRUD Task API built with FastAPI and PostgreSQL, fully containerized using Docker and Docker Compose.

## Features

* Create tasks
* Read tasks
* Update tasks
* Delete tasks
* PostgreSQL database persistence
* Dockerized application stack
* Environment-based configuration using `.env`
* Automatic database initialization
* Connection retry logic for container startup

## Tech Stack

* FastAPI
* PostgreSQL
* Docker
* Docker Compose
* Python

## Project Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd FlyRank-Week3
```

### 2. Create Environment File

Copy the example file:

```bash
cp .env.example .env
```

Example configuration:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/tasksdb
```

### 3. Start the Application

```bash
docker compose up --build
```

This starts:

* FastAPI application
* PostgreSQL database

### 4. Access the API

API:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

## Database Configuration

PostgreSQL runs inside Docker and is configured through Docker Compose.

The application connects using:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/tasksdb
```

A named Docker volume is used for persistent storage:

```yaml
volumes:
  postgres_data:
```

## Data Persistence Verification

The application uses a named Docker volume (`postgres_data`) to preserve PostgreSQL data between container restarts.

### Test Procedure

1. Start the application:

```bash
docker compose up --build
```

2. Create a new task:

```bash
curl -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Persistence Test"}'
```

Response:

```json
{"id":4,"title":"Persistence Test","done":false}
```

3. Stop the containers:

```bash
docker compose down
```

4. Restart the containers:

```bash
docker compose up --build
```

5. Retrieve all tasks:

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

The task remained available after the containers were restarted, confirming successful PostgreSQL persistence through the Docker volume.

## Architecture Update

The original storage implementation was replaced with a PostgreSQL repository while keeping the existing service and API layers unchanged.

Additional improvements include:

* PostgreSQL integration
* Docker Compose orchestration
* Connection retry logic
* Environment-based configuration
* Persistent Docker volume storage
* Repository pattern implementation
