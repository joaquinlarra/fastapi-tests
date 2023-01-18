def test_health_check(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_get_items_empty(client):
    res = client.get("/items")
    assert res.status_code == 200
    assert res.json() == []

def test_create_item_unauthorized(client):
    res = client.post("/items", json={
        "title": "Widget",
        "price": 19.99
    })
    assert res.status_code == 401

def test_create_and_get_item(client, auth_headers):
    # Create
    create_res = client.post("/items", json={
        "title": "Wireless Mouse",
        "description": "Ergonomic 2.4GHz mouse",
        "price": 29.99
    }, headers=auth_headers)
    assert create_res.status_code == 201
    item = create_res.json()
    assert item["id"] == 1
    assert item["title"] == "Wireless Mouse"

    # Get single
    get_res = client.get("/items/1")
    assert get_res.status_code == 200
    assert get_res.json()["title"] == "Wireless Mouse"

def test_get_nonexistent_item(client):
    res = client.get("/items/999")
    assert res.status_code == 404
