from client.crypto.signatures import (
    SignatureHandler
)


def test_invalid_signature():

    signing_key, verify_key = (
        SignatureHandler.generate_identity_keys()
    )

    message = b"hello"

    signature = (
        SignatureHandler.sign_message(
            signing_key,
            message
        )
    )

    tampered = b"hacked"

    assert (
        SignatureHandler.verify_signature(
            verify_key,
            tampered,
            signature
        )
        is False
    )