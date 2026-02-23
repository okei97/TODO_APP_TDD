from app.domain.todo import Todo
from app.infrastructure.todo_repository import save
import uuid

def create_todo(title: str) -> Todo:
    id = str(uuid.uuid4())
    todo = Todo(id, title)
    save(todo)
    return todo