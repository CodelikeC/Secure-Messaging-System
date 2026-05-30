from dataclasses import dataclass


@dataclass
class User:

    username: str

    public_key: str

    fingerprint: str

    verified: bool = False