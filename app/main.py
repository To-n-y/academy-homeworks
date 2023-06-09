from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

from app.routers.routerfriends import routerFriends
from app.routers.routeruser import routerUser

from scripts.create_db import main as create_database

chat_rooms = {}


def create_app():
    create_database()
    application = FastAPI()
    application.include_router(routerFriends, prefix="/friends")
    application.include_router(routerUser, prefix="/user")
    return application


app = create_app()


@app.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(f"You sent: {data}")
    await websocket.close()


@app.websocket("/ws/{chat_name}")
async def websocket_endpoint(websocket: WebSocket, chat_name: str):
    await websocket.accept()
    if chat_name not in chat_rooms:
        chat_rooms[chat_name] = []
    chat_rooms[chat_name].append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for ws in chat_rooms[chat_name]:
                if ws != websocket:
                    await ws.send_text(data)
    except WebSocketDisconnect:
        chat_rooms[chat_name].remove(websocket)
