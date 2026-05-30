from dataclasses import dataclass


@dataclass
class ContactVerification:

    username: str

    fingerprint: str

    verified: bool