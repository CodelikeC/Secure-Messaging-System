import asyncio
import time


class Heartbeat:

    def __init__(
        self,
        websocket_client,
        interval=30
    ):

        self.websocket_client = (
            websocket_client
        )

        self.interval = interval

        self.running = False

    async def start(self):

        self.running = True

        while self.running:

            packet = {
                "type": "heartbeat",
                "timestamp": int(
                    time.time()
                )
            }

            await self.websocket_client.send_packet(
                packet
            )

            await asyncio.sleep(
                self.interval
            )

    def stop(self):

        self.running = False