from client.storage.storage_manager import (
    StorageManager
)


class SessionStore:

    FILE_NAME = "sessions.json"

    def __init__(self):

        self.storage = StorageManager()

    def save_sessions(
        self,
        sessions
    ):

        self.storage.save_json(
            self.FILE_NAME,
            sessions
        )

    def load_sessions(self):

        data = self.storage.load_json(
            self.FILE_NAME
        )

        return data or {}