"""
Recipe: Mocking external HTTP services and integrations in FastAPI tests.
"""
from unittest.mock import patch, MagicMock

def fetch_payment_status(tx_id: str) -> dict:
    # Simulated external HTTP call
    raise NotImplementedError("Network calls must be mocked in tests")

def test_mock_external_service():
    with patch(f"{__name__}.fetch_payment_status") as mock_fetch:
        mock_fetch.return_value = {"id": "tx_123", "status": "succeeded", "amount": 5000}
        result = fetch_payment_status("tx_123")
        assert result["status"] == "succeeded"
        assert result["amount"] == 5000
        mock_fetch.assert_called_once_with("tx_123")
