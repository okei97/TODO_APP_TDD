from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_todo_success():
    response = client.post(
        "/todos",
        json={"title": "pytestからのTodo"}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["title"] == "pytestからのTodo"
    assert body["completed"] is False


def test_create_todo_without_title():
    response = client.post(
        "/todos",
        json={}
    )
    #入力して成立しない場合はインターフェース層で弾く。422エラーとなるべき。
    assert response.status_code == 422


def test_create_todo_empty_title():
    response = client.post(
        "/todos",
        json={"title": ""}
    )
    # 空文字は業務的に意味がないのでドメイン層で弾く。400エラーとなるべき。
    assert response.status_code == 400
