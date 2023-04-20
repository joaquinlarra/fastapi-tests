"""
Recipe: Overriding database / stateful dependency in FastAPI tests.
"""
from typing import Generator
import pytest

class FakeDatabaseSession:
    def __init__(self):
        self.storage = {}

    def add(self, key: str, val: dict):
        self.storage[key] = val

    def get(self, key: str):
        return self.storage.get(key)

def test_dependency_override_pattern():
    db = FakeDatabaseSession()
    db.add("item-1", {"name": "Widget", "price": 19.99})
    assert db.get("item-1")["name"] == "Widget"
    assert db.get("non-existent") is None
