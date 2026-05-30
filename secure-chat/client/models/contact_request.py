from dataclasses import dataclass


@dataclass
class ContactRequest:

    requester: str

    target: str

    timestamp: int