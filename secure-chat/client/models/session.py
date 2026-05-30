from dataclasses import dataclass


@dataclass
class Session:

    session_id: str

    local_user: str

    remote_user: str

    created_at: int

    expires_at: int