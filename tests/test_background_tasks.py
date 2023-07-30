"""
Recipe: Testing FastAPI BackgroundTasks execution synchronously in unit tests.
"""

def audit_log_action(user_id: int, action: str, log_buffer: list):
    log_buffer.append(f"user:{user_id} - action:{action}")

def test_background_task_execution():
    logs = []
    # Simulate background task scheduled during request
    audit_log_action(user_id=1, action="created_item", log_buffer=logs)
    assert len(logs) == 1
    assert "created_item" in logs[0]
