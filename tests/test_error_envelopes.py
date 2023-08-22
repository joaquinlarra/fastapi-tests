"""
Recipe: Standardizing and verifying error envelopes across microservice endpoints.
"""

def format_error_response(message: str, code: str, details: dict = None) -> dict:
    return {
        "error": {
            "code": code,
            "message": message,
            "details": details or {}
        }
    }

def test_error_envelope_structure():
    err = format_error_response("Resource not found", code="NOT_FOUND", details={"id": 404})
    assert "error" in err
    assert err["error"]["code"] == "NOT_FOUND"
    assert err["error"]["details"]["id"] == 404
