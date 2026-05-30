from dataclasses import dataclass


@dataclass
class Profile:

    username: str

    public_key: str

    fingerprint: str

    created_at: int