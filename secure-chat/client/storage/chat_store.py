from client.storage.storage_manager import (
    StorageManager
)


class ChatStore:

    FILE_NAME = "chat_history.json"

    def __init__(self):

        self.storage = StorageManager()

    def save_chat_history(
        self,
        history
    ):

        self.storage.save_json(
            self.FILE_NAME,
            history
        )

    def load_chat_history(self):

        data = self.storage.load_json(
            self.FILE_NAME
        )

        return data or {}