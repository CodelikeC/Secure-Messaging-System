from dataclasses import dataclass


@dataclass
class AuthToken:

    token: str

    expires_at: int | None = None