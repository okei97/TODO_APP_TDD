from fastapi.testclient import TestClient
from app.main import app
from app.infrastructure.todo_repository import clear_all

client = TestClient(app)

def setup_function():
    clear_all()

def test_get_todo_list_empty():
    response = client.get("/todos")

    assert response.status_code == 200
    assert response.json() == []

def test_get_todo_after_post():
    client.post("/todos", json={"title": "Test Todo"})

    response = client.get("/todos")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) == 1
    assert todos[0]["title"] == "Test Todo"