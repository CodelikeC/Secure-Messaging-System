from dataclasses import dataclass


@dataclass
class Contact:

    username: str

    public_key: str

    fingerprint: str

    verified: bool

    last_seen: int | None = None