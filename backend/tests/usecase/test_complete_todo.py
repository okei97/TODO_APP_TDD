import pytest
from app.infrastructure.todo_repository import clear_all, save
from app.domain.todo import Todo
from datetime import datetime

from app.usecase.complete_todo import complete_todo

def test_complete_todo_success(fixed_now):
    clear_all()
    todo = Todo("test_id", "test")
    save(todo)

    completed_todo = complete_todo(todo.id, fixed_now)
    assert completed_todo.completed is True
    assert completed_todo.completed_at == fixed_now

def test_complete_todo_unexisting_id(fixed_now):
    clear_all()
    with pytest.raises(ValueError):
        complete_todo("nonexistent_id", fixed_now)