# FastAPI Testing Recipes & Toolkit

[![Test Suite](https://github.com/joaquinlarra/fastapi-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/joaquinlarra/fastapi-tests/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)

Curated collection of testing patterns, reusable fixtures, and recipes for building bulletproof FastAPI microservices.

## Recipes Included
1. **Async & Sync Test Clients**: Best practices using `httpx.AsyncClient` and `starlette.testclient.TestClient`.
2. **Dependency Overrides**: Swapping out database sessions (`app.dependency_overrides`) with ephemeral SQLite engines.
3. **External Service Mocking**: Isolated HTTP and gRPC mocks using `unittest.mock`.
4. **Authentication & JWT**: Generating valid and expired tokens for role-based authorization tests.
5. **Background Tasks**: Verifying async task queues without executing real I/O.
6. **Rate Limiting & Headers**: Asserting rate-limiting headers and `429 Too Many Requests` behavior.

## Running Tests

```bash
pytest -v
```

## License
MIT License (c) 2022-2023 Joaquin Astelarra.
