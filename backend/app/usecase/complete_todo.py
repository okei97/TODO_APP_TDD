from app.domain.todo import Todo
from app.infrastructure.todo_repository import get,save

def complete_todo(id: str) -> Todo:
    todo = get(id)
    todo.complete()
    save(todo)
    return todo