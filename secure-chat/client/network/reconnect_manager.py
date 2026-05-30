import asyncio


class ReconnectManager:

    def __init__(
        self,
        websocket_client,
        max_retries=5
    ):

        self.websocket_client = (
            websocket_client
        )

        self.max_retries = max_retries

    async def reconnect(self):

        for attempt in range(
            self.max_retries
        ):

            try:

                await self.websocket_client.connect()

                return True

            except Exception:

                await asyncio.sleep(
                    2 ** attempt
                )

        return False