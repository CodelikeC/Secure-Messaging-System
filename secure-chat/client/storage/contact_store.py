from client.storage.storage_manager import (
    StorageManager
)


class ContactStore:

    FILE_NAME = "contacts.json"

    def __init__(self):

        self.storage = StorageManager()

    def save_contacts(
        self,
        contacts
    ):

        self.storage.save_json(
            self.FILE_NAME,
            contacts
        )

    def load_contacts(self):

        data = self.storage.load_json(
            self.FILE_NAME
        )

        return data or {}