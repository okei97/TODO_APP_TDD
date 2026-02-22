from app.domain.todo import Todo
from app.infrastructure.todo_repository import get,save
from datetime import datetime

def complete_todo(id: str, now: datetime) -> Todo:
    todo = get(id)
    todo.complete(now)
    save(todo)
    return todo