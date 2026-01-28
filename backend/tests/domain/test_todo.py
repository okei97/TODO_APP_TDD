import pytest
from app.domain.todo import Todo

def test_todo_empty_title():
    with pytest.raises(ValueError):
        Todo("")

def test_todo_initial_completed_false():
    todo = Todo("test")
    assert todo.completed is False
