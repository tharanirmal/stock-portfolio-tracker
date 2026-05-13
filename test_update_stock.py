def test_update_stock():
    # create stock first
    client.post("/stocks", json={"ticker": "AAPL", "shares": 10})

    # update it
    response = client.put("/stocks/AAPL", json={"shares": 25})

    # check success
    assert response.status_code == 200