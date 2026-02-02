from app.domain.todo import Todo

_todos: list[Todo] = []

def save(todo: Todo) -> None:
    _todos.append(todo)

def list_all() -> list[Todo]:
    return _todos
