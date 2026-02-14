from fastapi.testclient import TestClient
from app.main import app
from app.infrastructure.todo_repository import clear_all

client = TestClient(app)

def setup_function():
    clear_all()

def test_complete_todo_api():
    post_response = client.post("/todos", json={"title": "Incomplete Todo"})
    assert post_response.status_code == 200
    todo = post_response.json()
    todo_id = todo["id"]

    complete_response = client.patch(f"/todos/{todo_id}/complete")
    assert complete_response.status_code == 200
    completed_todo = complete_response.json()
    assert completed_todo["completed"] is True

    list_response = client.get("/todos")
    todos = list_response.json()
    assert len(todos) == 1
    assert todos[0]["completed"] is True