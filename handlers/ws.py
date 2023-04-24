from fastapi import WebSocket


class WebSocketEndpoint:
    async def __call__(self, websocket: WebSocket):
        await websocket.accept()
        data = await websocket.receive_text()
        await websocket.send_text(f"You sent: {data}")
        await websocket.close()


websocket_endpoint = WebSocketEndpoint()
