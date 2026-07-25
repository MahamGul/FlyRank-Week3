from database import (
    init_db,
    seed_data,
    get_all_tasks,
    get_task_by_id,
    create_task
)
from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse
init_db()
seed_data()
app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing tasks.",
    version="1.0"
)
@app.get(
    "/tasks",
    summary="Get all Tasks"
)
def get_tasks():
    return get_all_tasks()

@app.get(
    "/tasks/{task_id}",
    summary="Get a Task by ID"
)
def get_task(task_id: int):

    task = get_task_by_id(task_id)

    if task:
        return task

    return JSONResponse(
        status_code=404,
        content={"error": "Task not found"}
    )

class TaskCreate(BaseModel):
    title: Optional[str] = None

@app.post(
    "/tasks",
    summary="Create a new task",
    status_code=201
)
def add_task(task: TaskCreate):

    if task.title is None:
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required"}
        )

    if not task.title.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "Title cannot be empty"}
        )

    return create_task(task.title)