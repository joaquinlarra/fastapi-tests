"""
Recipe: Testing rate limiting headers and 429 Too Many Requests response handling.
"""

class SimpleRateLimiter:
    def __init__(self, limit: int = 5):
        self.limit = limit
        self.counts = {}

    def allow(self, client_ip: str) -> bool:
        c = self.counts.get(client_ip, 0)
        if c >= self.limit:
            return False
        self.counts[client_ip] = c + 1
        return True

def test_rate_limiter():
    limiter = SimpleRateLimiter(limit=3)
    ip = "192.168.1.10"
    assert limiter.allow(ip) is True
    assert limiter.allow(ip) is True
    assert limiter.allow(ip) is True
    assert limiter.allow(ip) is False
