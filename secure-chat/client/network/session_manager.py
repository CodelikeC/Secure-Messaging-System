from client.crypto.session import (
    SecureSession
)


class SessionManager:

    def __init__(self):

        self.sessions = {}

    def create_session(
        self,
        username: str
    ):

        session = SecureSession()

        session.initialize()

        self.sessions[username] = session

        return session

    def get_session(
        self,
        username: str
    ):

        return self.sessions.get(username)

    def remove_session(
        self,
        username: str
    ):

        if username in self.sessions:

            self.sessions[
                username
            ].destroy()

            del self.sessions[
                username
            ]