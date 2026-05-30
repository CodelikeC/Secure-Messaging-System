from client.crypto.aes import AESHandler


def test_encrypt_decrypt():

    key = AESHandler.generate_key()

    plaintext = "hello secure world"

    encrypted = AESHandler.encrypt(
        key,
        plaintext
    )

    decrypted = AESHandler.decrypt(
        key,
        encrypted["nonce"],
        encrypted["ciphertext"]
    )

    assert decrypted == plaintext