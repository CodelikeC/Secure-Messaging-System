from dataclasses import dataclass, field

from client.models.message import Message


@dataclass
class ChatHistory:

    contact: str

    messages: list[Message] = field(
        default_factory=list
    )

    def add_message(
        self,
        message: Message
    ):
        self.messages.append(message)