import pytest
from app.infrastructure.todo_repository import clear_all

@pytest.fixture(autouse=True)
def reset_repository():
    clear_all()