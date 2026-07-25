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