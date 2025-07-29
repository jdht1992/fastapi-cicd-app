from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_read_item(item_id: int = 123):
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": 123, "query_param": None}


def test_read_item_with_query_param(item_id: int = 456, query_param: str = "test"):
    response = client.get(f"/items/{item_id}?query_param={query_param}")
    assert response.status_code == 200
    assert response.json() == {"item_id": 456, "query_param": "test"}


