from database import init_db, seed_data
from repositories.sqlite_repository import SQLiteTaskRepository

from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Response

init_db()
seed_data()
repository = SQLiteTaskRepository()
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
    return repository.get_all_tasks()

@app.get(
    "/tasks/{task_id}",
    summary="Get a Task by ID"
)
def get_task(task_id: int):

    task = repository.get_task_by_id(task_id)

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

    return repository.create_task(task.title)

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

@app.put(
    "/tasks/{task_id}",
    summary="Update a task"
)
def update_task_endpoint(task_id: int, updated_data: TaskUpdate):

    if (
        updated_data.title is None
        and updated_data.done is None
    ):
        return JSONResponse(
            status_code=400,
            content={"error": "Request body cannot be empty"}
        )

    if (
        updated_data.title is not None
        and not updated_data.title.strip()
    ):
        return JSONResponse(
            status_code=400,
            content={"error": "Title cannot be empty"}
        )

    updated_task = repository.update_task(
        task_id,
        updated_data.title,
        updated_data.done
    )

    if updated_task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"}
        )

    return updated_task

@app.delete(
    "/tasks/{task_id}",
    summary="Delete a task"
)
def delete_task_endpoint(task_id: int):

    deleted = repository.delete_task(task_id)

    if not deleted:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"}
        )

    return Response(status_code=204)