import pytest
from app.infrastructure.todo_repository import clear_all, get

from app.usecase.create_todo import create_todo

def test_create_todo_saves_todo ():
    clear_all()
    todo = create_todo("test")

    saved_todo = get(todo.id)
    assert saved_todo is not None
    assert saved_todo.title == "test"