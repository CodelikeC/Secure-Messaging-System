import json
from pathlib import Path


class StorageManager:

    def __init__(self):

        self.storage_dir = Path("storage")

        self.storage_dir.mkdir(
            exist_ok=True
        )

    def save_json(
        self,
        filename: str,
        data: dict
    ):

        filepath = (
            self.storage_dir / filename
        )

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

    def load_json(
        self,
        filename: str
    ):

        filepath = (
            self.storage_dir / filename
        )

        if not filepath.exists():
            return None

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)