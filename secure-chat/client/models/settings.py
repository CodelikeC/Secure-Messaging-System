from dataclasses import dataclass


@dataclass
class Settings:

    notifications_enabled: bool = True

    auto_lock_minutes: int = 15

    auto_verify_contacts: bool = False