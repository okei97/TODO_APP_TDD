from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.interface.schema import CreateTodoRequest
from app.usecase.create_todo import create_todo
from app.usecase.list_todos import list_todos
from app.usecase.complete_todo import complete_todo
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(ValueError)
def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )

@app.post("/todos")
def create_todo_api(req: CreateTodoRequest):
    todo = create_todo(req.title)
    return todo

@app.get("/todos")
def list_todos_api():
    return list_todos()

@app.patch("/todos/{todo_id}/complete")
def complete_todo_api(todo_id: str):
    now = datetime.now()
    todo = complete_todo(todo_id, now)
    return todo