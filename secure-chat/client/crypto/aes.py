from cryptography.hazmat.primitives.ciphers.aead import AESGCM

import os
import base64


class AESHandler:

    @staticmethod
    def generate_key():

        return AESGCM.generate_key(
            bit_length=256
        )

    @staticmethod
    def encrypt(
        key: bytes,
        plaintext: str
    ):

        aesgcm = AESGCM(key)

        nonce = os.urandom(12)

        ciphertext = aesgcm.encrypt(
            nonce,
            plaintext.encode(),
            None
        )

        return {
            "nonce": base64.b64encode(nonce).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode()
        }

    @staticmethod
    def decrypt(
        key: bytes,
        nonce: str,
        ciphertext: str
    ):

        aesgcm = AESGCM(key)

        decoded_nonce = base64.b64decode(nonce)

        decoded_ciphertext = base64.b64decode(ciphertext)

        plaintext = aesgcm.decrypt(
            decoded_nonce,
            decoded_ciphertext,
            None
        )

        return plaintext.decode()