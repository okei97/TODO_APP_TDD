from app.domain.todo import Todo
from app.infrastructure.todo_repository import list_all

def list_todos() -> list[Todo]:
    return list_all()