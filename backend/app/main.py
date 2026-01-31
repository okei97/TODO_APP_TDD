from fastapi import FastAPI
from app.interface.schema import CreateTodoRequest
from app.usecase.create_todo import create_todo

app = FastAPI()

@app.post("/todos")
def create_todo_api(req: CreateTodoRequest):
    todo = create_todo(req.title)
    return todo