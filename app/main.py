from fastapi import FastAPI, HTTPException
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from .src.databaseConnection import init_db
from .src.schemas import TaskCreate, TaskUpdate, TaskResponse
from .src import crud

app = FastAPI(title="ToDo API")

# ---------- CORS ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # frontend (Vite)
        # "https://your-frontend-domain.com"  # add after deployment
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- STARTUP ----------
@app.on_event("startup")
def startup_event():
    try:
        init_db()
    except RuntimeError as e:
        # startup errors should fail the app, not return HTTP response
        raise RuntimeError(str(e))


# ---------- CREATE ----------
@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task_api(task: TaskCreate):
    try:
        return crud.create_task(task)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------- READ ALL ----------
@app.get("/tasks", response_model=List[TaskResponse])
def read_all_tasks():
    try:
        return crud.get_tasks()
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------- READ ONE ----------
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int):
    try:
        task = crud.get_task_by_id(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------- UPDATE ----------
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task_api(task_id: int, task: TaskUpdate):
    try:
        updated = crud.update_task(task_id, task)
        if not updated:
            raise HTTPException(
                status_code=404,
                detail="Task not found or empty update payload"
            )
        return updated
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------- DELETE ----------
@app.delete("/tasks/{task_id}")
def delete_task_api(task_id: int):
    try:
        deleted = crud.delete_task(task_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task deleted successfully"}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
