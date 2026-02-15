import pytest
from app.infrastructure.todo_repository import clear_all, save
from app.domain.todo import Todo

from app.usecase.complete_todo import complete_todo

def test_complete_todo_success():
    clear_all()
    todo = Todo("test")
    save(todo)

    completed_todo = complete_todo(todo.id)
    assert completed_todo.completed is True