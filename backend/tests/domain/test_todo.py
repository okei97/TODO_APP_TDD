import pytest
from app.domain.todo import Todo

def test_todo_empty_title():
    with pytest.raises(ValueError):
        Todo("")

def test_todo_initial_completed_false():
    todo = Todo("test")
    assert todo.completed is False

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