from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK


def test_select():
    response = client.get("/user/users")
    assert response.status_code == status.HTTP_200_OK


def test_select_by_id():
    response = client.get("/user?id=1")
    assert response.status_code == status.HTTP_200_OK
