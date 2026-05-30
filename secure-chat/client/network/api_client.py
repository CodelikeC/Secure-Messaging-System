import requests


class APIClient:

    def __init__(self, base_url: str):

        self.base_url = base_url.rstrip("/")

    def register(
        self,
        username: str,
        password: str,
        public_key: str
    ):

        response = requests.post(
            f"{self.base_url}/auth/register",
            json={
                "username": username,
                "password": password,
                "public_key": public_key
            }
        )

        return response.json()

    def login(
        self,
        username: str,
        password: str
    ):

        response = requests.post(
            f"{self.base_url}/auth/login",
            json={
                "username": username,
                "password": password
            }
        )

        return response.json()

    def get_public_key(
        self,
        username: str
    ):

        response = requests.get(
            f"{self.base_url}/auth/public-key/{username}"
        )

        return response.json()