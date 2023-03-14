# fastapi-tests

[![CI](https://img.shields.io/badge/CI-passing-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-0.88-teal.svg)]()

A reference test suite and pattern guide for unit, integration, and contract testing of FastAPI microservices.

## Patterns Included

1. **Synchronous Testing**: Using `fastapi.testclient.TestClient`.
2. **Asynchronous Testing**: Non-blocking end-to-end testing with `httpx.AsyncClient`.
3. **Authentication Fixtures**: Bearer token injection and unauthorized header validation.
4. **Database Isolation**: Fixtures guaranteeing atomic state cleanup between test cases.
5. **Schema Validation**: Testing HTTP 422 edge cases and boundary conditions.

---

## Running the Tests

```bash
pip install -r requirements.txt
pytest -v
```

---

## License
MIT © [Joaquin Astelarra](https://github.com/joaquinlarra)
