from client.crypto.session import (
    SecureSession
)


def test_session_lifecycle():

    session = SecureSession()

    session.initialize()

    assert (
        session.private_key
        is not None
    )

    session.destroy()

    assert (
        session.private_key
        is None
    )