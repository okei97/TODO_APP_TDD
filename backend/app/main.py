from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.interface.schema import CreateTodoRequest
from app.usecase.create_todo import create_todo
from app.usecase.list_todos import list_todos

app = FastAPI()

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