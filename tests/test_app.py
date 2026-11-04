import pytest
from app import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app()
    app.config["TESTING"] = True
    app.config["DATABASE"] = str(tmp_path / "test_tasks.db")

    with app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_add_task(client):
    response = client.post("/add", data={
        "title": "Complete Assignment",
        "description": "Finish Flask development",
        "priority": "Medium"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Complete Assignment" in response.data


def test_complete_task(client):
    client.post("/add", data={
        "title": "Test Task",
        "description": "Testing task completion"
    })

    response = client.post("/complete/1", follow_redirects=True)

    assert response.status_code == 200
    assert b"Completed" in response.data


def test_edit_task(client):
    client.post("/add", data={
        "title": "Old Task",
        "description": "Old description"
    })

    response = client.post("/edit/1", data={
        "title": "Updated Task",
        "description": "Updated description"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Updated Task" in response.data


def test_delete_task(client):
    client.post("/add", data={
        "title": "Task to Delete",
        "description": "Delete this task"
    })

    response = client.post("/delete/1", follow_redirects=True)

    assert response.status_code == 200
    assert b"Task to Delete" not in response.data


@pytest.mark.parametrize("priority", ["High", "Medium", "Low"])
def test_task_priorities(client, priority):
    response = client.post("/add", data={
        "title": "Priority Test",
        "description": "Testing task priority",
        "priority": priority
    }, follow_redirects=True)

    assert response.status_code == 200
    assert priority.encode() in response.data
    assert b"Priority Test" in response.data
