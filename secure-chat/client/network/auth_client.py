class AuthClient:

    def __init__(self):

        self.token = None

    def set_token(
        self,
        token: str
    ):

        self.token = token

    def get_token(self):

        return self.token

    def is_authenticated(self):

        return self.token is not None

    def logout(self):

        self.token = None