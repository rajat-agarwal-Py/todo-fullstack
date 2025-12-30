import os
import pytest
from fastapi.testclient import TestClient

# IMPORTANT: set test DB before importing app
os.environ["DB_NAME"] = "todo_test.db"

from app.main import app
from app.src.databaseConnection import init_db

TEST_DB = "todo_test.db"


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    init_db()
    yield

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


@pytest.fixture()
def client():
    return TestClient(app)
