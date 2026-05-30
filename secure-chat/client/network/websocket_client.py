import asyncio
import json
import websockets


class WebSocketClient:

    def __init__(
        self,
        username: str,
        server_url: str
    ):

        self.username = username

        self.server_url = server_url

        self.websocket = None

    async def connect(self):

        self.websocket = await websockets.connect(
            f"{self.server_url}/ws/{self.username}"
        )

    async def disconnect(self):

        if self.websocket:
            await self.websocket.close()

    async def send_packet(
        self,
        packet: dict
    ):

        await self.websocket.send(
            json.dumps(packet)
        )

    async def receive_packet(self):

        data = await self.websocket.recv()

        return json.loads(data)