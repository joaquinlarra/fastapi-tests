"""
Recipe: Testing pagination, offset/limit parameters, and edge cases.
"""

def paginate(items: list, offset: int = 0, limit: int = 10) -> dict:
    total = len(items)
    page_items = items[offset : offset + limit]
    return {
        "items": page_items,
        "total": total,
        "offset": offset,
        "limit": limit,
        "has_more": (offset + limit) < total
    }

def test_pagination_defaults():
    dataset = list(range(25))
    page = paginate(dataset, offset=0, limit=10)
    assert len(page["items"]) == 10
    assert page["items"][0] == 0
    assert page["has_more"] is True

def test_pagination_last_page():
    dataset = list(range(25))
    page = paginate(dataset, offset=20, limit=10)
    assert len(page["items"]) == 5
    assert page["has_more"] is False
