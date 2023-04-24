import pytest
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


def test_websockets():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("HelloWorld")
        data = websocket.receive_text()
        assert data == "You sent: HelloWorld"


@pytest.mark.asyncio
async def test_chat_room():
    client2 = TestClient(app)
    with client.websocket_connect('ws://localhost:8000/ws/test') as ws1:
        with client2.websocket_connect('ws://localhost:8000/ws/test') as ws2:
            ws1.send_text('Hello from ws1')
            ws2.send_text('Hello from ws2')
            message1 = ws1.receive_text()
            message2 = ws2.receive_text()
            assert message1 == 'Hello from ws2'
            assert message2 == 'Hello from ws1'
        ws2.close()
    ws1.close()
