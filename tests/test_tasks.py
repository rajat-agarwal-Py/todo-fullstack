"""
Integration tests for Task APIs

These tests verify:
- Request validation
- Happy paths for CRUD
- Edge cases (empty update, missing records)
- Proper HTTP status codes

DB used: todo_test.db (configured via conftest.py)
"""

# ---------- CREATE ----------

def test_create_task_success(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Test Description",
            "due_date": "2025-12-31"
        }
    )

    assert response.status_code == 201

    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["due_date"] == "2025-12-31"
    assert data["status"] == "pending"


def test_create_task_validation_error(client):
    response = client.post(
        "/tasks",
        json={
            "title": ""  # invalid: min_length=1
        }
    )

    assert response.status_code == 422


# ---------- READ ALL ----------

def test_get_all_tasks(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


# ---------- READ ONE ----------

def test_get_task_by_id_success(client):
    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_task_by_id_not_found(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


# ---------- UPDATE ----------

def test_update_task_success(client):
    response = client.put(
        "/tasks/1",
        json={
            "status": "completed"
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] == "completed"


def test_update_task_empty_payload(client):
    response = client.put(
        "/tasks/1",
        json={}
    )

    assert response.status_code == 404
    assert "empty update payload" in response.json()["detail"]


def test_update_task_not_found(client):
    response = client.put(
        "/tasks/999",
        json={
            "status": "completed"
        }
    )

    assert response.status_code == 404


# ---------- DELETE ----------

def test_delete_task_success(client):
    response = client.delete("/tasks/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"


def test_delete_task_not_found(client):
    response = client.delete("/tasks/999")

    assert response.status_code == 404
