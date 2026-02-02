from app.domain.todo import Todo
from backend.app.infrastructure.todo_repository import save

def create_todo(title: str) -> Todo:
    todo = Todo(title)
    save(todo)
    return todo