from fastapi import APIRouter, WebSocket
from handlers.ws import websocket_endpoint

routerws = APIRouter()


@routerws.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_endpoint(websocket)
