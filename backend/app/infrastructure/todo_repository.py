from app.domain.todo import Todo

_todos: dict[str, Todo] = {}

def save(todo: Todo) -> None:
    _todos[todo.id] = todo

def get(id: str) -> Todo:
    try:
        return _todos[id]
    except KeyError:
        raise ValueError(f"Todo with id {id} not found")

def list_all() -> list[Todo]:
    return list(_todos.values())

def clear_all() -> None:
    _todos.clear()