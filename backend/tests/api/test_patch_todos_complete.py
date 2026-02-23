from fastapi.testclient import TestClient
from app.main import app
from app.infrastructure.todo_repository import clear_all
from datetime import datetime

client = TestClient(app)

def setup_function():
    clear_all()

def test_patch_complete_success():
    post_response = client.post("/todos", json={"title": "Incomplete Todo"})
    assert post_response.status_code == 201
    todo = post_response.json()
    todo_id = todo["id"]

    t0 = datetime.now()
    complete_response = client.patch(f"/todos/{todo_id}/complete")
    t1 = datetime.now()
    assert complete_response.status_code == 200
    completed_todo = complete_response.json()
    assert completed_todo["completed"] is True
    completed_at = datetime.fromisoformat(completed_todo["completed_at"])
    assert t0 <= completed_at <= t1

    list_response = client.get("/todos")
    todos = list_response.json()
    assert len(todos) == 1
    assert todos[0]["completed"] is True

def test_patch_complete_when_already_completed():
    post_response = client.post("/todos", json={"title": "Already Completed Todo"})
    assert post_response.status_code == 201
    todo = post_response.json()
    todo_id = todo["id"]

    complete_response1 = client.patch(f"/todos/{todo_id}/complete")
    assert complete_response1.status_code == 200

    complete_response2 = client.patch(f"/todos/{todo_id}/complete")
    assert complete_response2.status_code == 400