from fastapi.testclient import TestClient
from app import app
client = TestClient(app)
def test_add_stock():
    response = client.post("/stocks", json={"ticker": "AAPL", "shares": 10})
    assert response.status_code == 200
    assert "AAPL" in response.json()["message"]
def test_get_stocks():
    client.post("/stocks", json={"ticker": "GOOG", "shares": 5})
    response = client.get("/stocks")
    assert response.status_code == 200
def test_update_stock():
    client.post("/stocks", json={"ticker": "MSFT", "shares": 10})
    response = client.put("/stocks/MSFT", json={"shares": 25})
    assert response.status_code == 200

def test_delete_stock():
    client.post("/stocks", json={"ticker": "TSLA", "shares": 10})
    response = client.delete("/stocks/TSLA")
    assert response.status_code == 200
    assert response.json()["message"] == "Removed TSLA from portfolio"

    assert response.status_code == 200
    assert response.json()["message"] == "Removed AAPL from portfolio"