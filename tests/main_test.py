import pytest
import websockets
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
    async with websockets.connect('ws://localhost:8000/ws/test') as ws1:
        async with websockets.connect('ws://localhost:8000/ws/test') as ws2:
            await ws1.send('Hello from ws1')
            await ws2.send('Hello from ws2')
            message1 = await ws1.recv()
            message2 = await ws2.recv()
            assert message1 == 'Hello from ws2'
            assert message2 == 'Hello from ws1'
        assert ws2.closed
    assert ws1.closed
