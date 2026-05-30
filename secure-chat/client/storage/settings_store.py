from client.storage.storage_manager import (
    StorageManager
)


class SettingsStore:

    FILE_NAME = "settings.json"

    def __init__(self):

        self.storage = StorageManager()

    def save_settings(
        self,
        settings
    ):

        self.storage.save_json(
            self.FILE_NAME,
            settings
        )

    def load_settings(self):

        data = self.storage.load_json(
            self.FILE_NAME
        )

        return data or {}