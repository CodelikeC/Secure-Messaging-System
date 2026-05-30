from client.crypto.aes import (
    AESHandler
)


def test_end_to_end_flow():

    key = AESHandler.generate_key()

    plaintext = (
        "hello secure messaging"
    )

    encrypted = (
        AESHandler.encrypt(
            key,
            plaintext
        )
    )

    decrypted = (
        AESHandler.decrypt(
            key,
            encrypted["nonce"],
            encrypted["ciphertext"]
        )
    )

    assert decrypted == plaintext