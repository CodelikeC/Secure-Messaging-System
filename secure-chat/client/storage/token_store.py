from client.storage.storage_manager import (
    StorageManager
)


class TokenStore:

    FILE_NAME = "token.json"

    def __init__(self):

        self.storage = StorageManager()

    def save_token(
        self,
        token: str
    ):

        self.storage.save_json(
            self.FILE_NAME,
            {
                "token": token
            }
        )

    def load_token(self):

        data = self.storage.load_json(
            self.FILE_NAME
        )

        if not data:
            return None

        return data.get("token")