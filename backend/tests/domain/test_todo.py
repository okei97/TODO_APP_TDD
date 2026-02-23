import pytest
from app.domain.todo import Todo
from datetime import datetime

def test_todo_empty_title():
    with pytest.raises(ValueError):
        Todo("test_id", "")

def test_todo_initial_state():
    todo = Todo("test_id", "test")
    assert todo.completed is False
    assert todo.completed_at is None

# titleが1文字の場合のテストを追加
def test_todo_title_one_character():
    todo = Todo("test_id", "A")
    assert todo.title == "A"

def test_todo_title_max_length():
    max_length_title = "A" * 100
    todo = Todo("test_id", max_length_title)
    assert todo.title == max_length_title

def test_todo_title_exceeds_max_length():
    too_long_title = "A" * 101
    with pytest.raises(ValueError):
        Todo("test_id", too_long_title)

def test_todo_completed_sets_true():
    todo = Todo("test_id", "test")
    now = datetime(2026, 2, 22, 15, 30)
    todo.complete(now)
    assert todo.completed is True
    assert todo.completed_at == now

def test_todo_complete_when_already_completed_raises_error():
    todo = Todo("test_id", "test")
    now = datetime(2026, 2, 22, 15, 30)
    todo.complete(now)
    with pytest.raises(ValueError):
        todo.complete(now)

def test_todo_completed_at():
    todo = Todo("test_id", "test")
    assert todo.completed_at is None