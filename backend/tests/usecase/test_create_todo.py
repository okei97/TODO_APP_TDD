import pytest
from app.usecase.create_todo import create_todo

def test_create_todo_success():
  todo = create_todo("Test Todo")
  assert todo.title == "Test Todo"
  assert todo.completed is False

def test_create_todo_empty_title():
    with pytest.raises(ValueError):
        create_todo("")
