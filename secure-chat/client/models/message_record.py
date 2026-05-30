from dataclasses import dataclass

from client.models.message_status import (
    MessageStatus
)


@dataclass
class MessageRecord:

    message_id: str

    sender: str

    receiver: str

    content: str

    timestamp: int

    status: MessageStatus