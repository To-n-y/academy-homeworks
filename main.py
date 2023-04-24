from fastapi import FastAPI, WebSocket

from routers.routerfriends import routerFriends
from routers.routeruser import routerUser

app = FastAPI()

app.include_router(routerUser, prefix="/user")
app.include_router(routerFriends, prefix="/friends")


@app.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(f"You send: {data}")
    await websocket.close()
