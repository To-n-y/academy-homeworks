from fastapi import FastAPI, WebSocket

from routers.routerfriends import routerFriends
from routers.routeruser import routerUser

app = FastAPI()


@app.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(f"You sent: {data}")
    await websocket.close()


app.include_router(routerFriends, prefix="/friends")
app.include_router(routerUser, prefix="/user")
