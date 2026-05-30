from dataclasses import dataclass


@dataclass
class RegisterResponse:

    success: bool

    message: str