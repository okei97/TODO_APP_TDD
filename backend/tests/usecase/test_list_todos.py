import pytest
from app.infrastructure.todo_repository import clear_all, save
from app.domain.todo import Todo

from app.usecase.list_todos import list_todos

def test_list_todos_returns_saved_todos():
    clear_all()
    todo = Todo("test")
    save(todo)

    todos = list_todos()
    assert len(todos) == 1
    assert todos[0].title == "test"
