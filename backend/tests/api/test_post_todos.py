from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_post_todo_success():
    response = client.post(
        "/todos",
        json={"title": "pytestからのTodo"}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["title"] == "pytestからのTodo"
    assert body["completed"] is False

def test_post_todo_title_one_character():
    response = client.post(
        "/todos",
        json={"title": "A"}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["title"] == "A"

def test_post_todo_title_max_length():
    max_length_title = "A" * 100
    response = client.post(
        "/todos",
        json={"title": max_length_title}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["title"] == max_length_title


def test_post_todo_without_title():
    response = client.post(
        "/todos",
        json={}
    )
    #入力して成立しない場合はインターフェース層で弾く。422エラーとなるべき。
    assert response.status_code == 422


def test_post_todo_empty_title():
    response = client.post(
        "/todos",
        json={"title": ""}
    )
    # 空文字は業務的に意味がないのでドメイン層で弾く。400エラーとなるべき。
    assert response.status_code == 400

def test_post_todo_title_exceeds_max_length():
    too_long_title = "A" * 101
    response = client.post(
        "/todos",
        json={"title": too_long_title}
    )
    # タイトルが最大長を超える場合はドメイン層で弾く。400エラーとなるべき。
    assert response.status_code == 400

def test_post_todo_has_id():
    response = client.post(
        "/todos",
        json={"title": "Todo with ID"}
    )

    assert response.status_code == 200

    body = response.json()
    assert "id" in body
    assert isinstance(body["id"], str)