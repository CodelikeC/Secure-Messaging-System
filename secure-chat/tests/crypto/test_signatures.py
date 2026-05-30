from client.crypto.signatures import (
    SignatureHandler
)


def test_signature():

    signing_key, verify_key = (
        SignatureHandler.generate_identity_keys()
    )

    message = b"secure-message"

    signature = (
        SignatureHandler.sign_message(
            signing_key,
            message
        )
    )

    assert (
        SignatureHandler.verify_signature(
            verify_key,
            message,
            signature
        )
        is True
    )