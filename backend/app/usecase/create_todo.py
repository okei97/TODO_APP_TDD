from app.domain.todo import Todo

def create_todo(title: str) -> Todo:
    return Todo(title)