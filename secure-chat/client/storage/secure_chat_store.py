from client.crypto.storage_crypto import (
    SecureStorageCrypto
)

from client.storage.storage_manager import (
    StorageManager
)


class SecureChatStore:

    FILE_NAME = "secure_chats.json"

    def __init__(self):

        self.storage = StorageManager()

    def save(
        self,
        password,
        plaintext_json
    ):

        encrypted = (
            SecureStorageCrypto.encrypt_data(
                password,
                plaintext_json
            )
        )

        self.storage.save_json(
            self.FILE_NAME,
            encrypted
        )

    def load(
        self,
        password
    ):

        encrypted = (
            self.storage.load_json(
                self.FILE_NAME
            )
        )

        if not encrypted:
            return None

        return (
            SecureStorageCrypto.decrypt_data(
                password=password,
                salt=encrypted["salt"],
                nonce=encrypted["nonce"],
                ciphertext=encrypted["ciphertext"]
            )
        )