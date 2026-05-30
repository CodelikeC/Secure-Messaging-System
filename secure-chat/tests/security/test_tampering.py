from client.crypto.aes import AESHandler

import pytest


def test_ciphertext_tampering():

    key = AESHandler.generate_key()

    encrypted = AESHandler.encrypt(
        key,
        "secret"
    )

    bad_ciphertext = (
        encrypted["ciphertext"][:-4]
        + "AAAA"
    )

    with pytest.raises(Exception):

        AESHandler.decrypt(
            key,
            encrypted["nonce"],
            bad_ciphertext
        )