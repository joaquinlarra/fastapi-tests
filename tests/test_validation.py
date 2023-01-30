def test_create_item_invalid_payload(client, auth_headers):
    # Missing price
    res = client.post("/items", json={"title": "Test"}, headers=auth_headers)
    assert res.status_code == 422

    # Negative price
    res = client.post("/items", json={"title": "Test", "price": -5.0}, headers=auth_headers)
    assert res.status_code == 422

    # Empty title
    res = client.post("/items", json={"title": "", "price": 10.0}, headers=auth_headers)
    assert res.status_code == 422
