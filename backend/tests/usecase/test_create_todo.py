import pytest
from app.infrastructure.todo_repository import get

from app.usecase.create_todo import create_todo

def test_create_todo_saves_todo ():
    todo = create_todo("test")

    saved_todo = get(todo.id)
    assert saved_todo is not None
    assert saved_todo.title == "test"

def test_todo_id_auto_generated():
    todo1 = create_todo("test1")
    todo2 = create_todo("test2")

    assert todo1.id is not None
    assert todo2.id is not None
    assert isinstance(todo1.id, str)
    assert isinstance(todo2.id, str)
    assert todo1.id != todo2.id