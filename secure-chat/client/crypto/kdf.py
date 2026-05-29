from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

from argon2.low_level import (
    hash_secret_raw,
    Type
)

import os


class KeyDerivation:

    @staticmethod
    def derive_session_key(shared_secret: bytes):

        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b"secure-messaging-session"
        )

        return hkdf.derive(shared_secret)

    @staticmethod
    def derive_storage_key(
        password: str,
        salt: bytes = None
    ):

        if salt is None:
            salt = os.urandom(16)

        key = hash_secret_raw(
            secret=password.encode(),
            salt=salt,
            time_cost=3,
            memory_cost=65536,
            parallelism=4,
            hash_len=32,
            type=Type.ID
        )

        return {
            "key": key,
            "salt": salt
        }