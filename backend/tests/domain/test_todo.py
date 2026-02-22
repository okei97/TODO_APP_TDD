import pytest
from app.domain.todo import Todo
from datetime import datetime

def test_todo_empty_title():
    with pytest.raises(ValueError):
        Todo("")

def test_todo_initial_state():
    todo = Todo("test")
    assert todo.completed is False
    assert todo.completed_at is None

# titleが1文字の場合のテストを追加
def test_todo_title_one_character():
    todo = Todo("A")
    assert todo.title == "A"

def test_todo_title_max_length():
    max_length_title = "A" * 100
    todo = Todo(max_length_title)
    assert todo.title == max_length_title

def test_todo_title_exceeds_max_length():
    too_long_title = "A" * 101
    with pytest.raises(ValueError):
        Todo(too_long_title)

def test_todo_id_auto_generated():
    todo1 = Todo("test1")
    todo2 = Todo("test2")
    assert todo1.id is not None
    assert todo2.id is not None
    assert isinstance(todo1.id, str)
    assert isinstance(todo2.id, str)
    assert todo1.id != todo2.id

def test_todo_completed_sets_true():
    todo = Todo("test")
    now = datetime(2026, 2, 22, 15, 30)
    todo.complete(now)
    assert todo.completed is True
    assert todo.completed_at == now

def test_todo_complete_when_already_completed_raises_error():
    todo = Todo("test")
    now = datetime(2026, 2, 22, 15, 30)
    todo.complete(now)
    with pytest.raises(ValueError):
        todo.complete(now)

def test_todo_completed_at():
    todo = Todo("test")
    assert todo.completed_at is None