from dataclasses import dataclass


@dataclass
class Device:

    device_id: str

    device_name: str

    registered_at: int