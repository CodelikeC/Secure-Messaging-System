from enum import Enum


class MessageStatus(Enum):

    PENDING = "pending"

    SENT = "sent"

    DELIVERED = "delivered"

    RECEIVED = "received"

    FAILED = "failed"