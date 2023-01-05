import pytest
from fastapi.testclient import TestClient
from app.main import app, ITEMS_DB

@pytest.fixture(autouse=True)
def clean_db():
    ITEMS_DB.clear()
    yield
    ITEMS_DB.clear()

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_headers():
    return {"Authorization": "Bearer admin"}
