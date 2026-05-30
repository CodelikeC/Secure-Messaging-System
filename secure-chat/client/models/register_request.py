from dataclasses import dataclass


@dataclass
class RegisterRequest:

    username: str

    password: str

    public_key: str