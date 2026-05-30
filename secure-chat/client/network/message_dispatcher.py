class MessageDispatcher:

    def __init__(self):

        self.handlers = {}

    def register_handler(
        self,
        message_type,
        callback
    ):

        self.handlers[
            message_type
        ] = callback

    async def dispatch(
        self,
        packet
    ):

        message_type = packet.get(
            "type",
            "message"
        )

        if (
            message_type
            in self.handlers
        ):

            await self.handlers[
                message_type
            ](packet)