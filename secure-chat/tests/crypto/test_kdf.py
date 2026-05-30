from client.crypto.kdf import (
    KeyDerivation
)


def test_session_key_generation():

    secret = b"shared-secret"

    key = (
        KeyDerivation.derive_session_key(
            secret
        )
    )

    assert len(key) == 32