import pytest
from datetime import datetime

@pytest.fixture
def fixed_now():
    return datetime(2026, 2, 22, 15, 30)