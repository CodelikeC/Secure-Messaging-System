from enum import Enum


class ApplicationState(Enum):

    STARTING = "starting"

    AUTHENTICATED = "authenticated"

    CONNECTING = "connecting"

    CONNECTED = "connected"

    DISCONNECTED = "disconnected"

    LOCKED = "locked"

    EXITING = "exiting"