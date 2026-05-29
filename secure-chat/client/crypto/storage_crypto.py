from client.crypto.aes import AESHandler
from client.crypto.kdf import KeyDerivation


class SecureStorageCrypto:

    @staticmethod
    def encrypt_data(
        password: str,
        plaintext: str
    ):

        derived = (
            KeyDerivation.derive_storage_key(
                password
            )
        )

        encrypted = AESHandler.encrypt(
            derived["key"],
            plaintext
        )

        return {
            "salt": derived["salt"].hex(),
            "nonce": encrypted["nonce"],
            "ciphertext": encrypted["ciphertext"]
        }

    @staticmethod
    def decrypt_data(
        password: str,
        salt: str,
        nonce: str,
        ciphertext: str
    ):

        derived = (
            KeyDerivation.derive_storage_key(
                password,
                bytes.fromhex(salt)
            )
        )

        return AESHandler.decrypt(
            derived["key"],
            nonce,
            ciphertext
        )