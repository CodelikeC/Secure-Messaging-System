import asyncio

from client.ui.console import (
    ConsoleUI
)

from client.network.api_client import (
    APIClient
)

from client.network.auth_client import (
    AuthClient
)

from client.storage.token_store import (
    TokenStore
)


SERVER_URL = (
    "http://localhost:8000"
)

WS_URL = (
    "ws://localhost:8000"
)


class SecureMessagingApp:

    def __init__(self):

        self.api = APIClient(
            SERVER_URL
        )

        self.auth = AuthClient()

        self.token_store = (
            TokenStore()
        )

    def register(self):

        username = (
            ConsoleUI.input_username()
        )

        password = (
            ConsoleUI.input_password()
        )

        response = self.api.register(
            username=username,
            password=password,
            public_key="TEMP_PUBLIC_KEY"
        )

        ConsoleUI.show(response)

    def login(self):

        username = (
            ConsoleUI.input_username()
        )

        password = (
            ConsoleUI.input_password()
        )

        response = self.api.login(
            username,
            password
        )

        token = response.get(
            "token"
        )

        if token:

            self.auth.set_token(
                token
            )

            self.token_store.save_token(
                token
            )

            ConsoleUI.show(
                "Login successful"
            )

        else:

            ConsoleUI.show(
                "Login failed"
            )

    async def run(self):

        ConsoleUI.banner()

        while True:

            ConsoleUI.menu()

            choice = input(
                "Select: "
            )

            if choice == "1":
                self.register()

            elif choice == "2":
                self.login()

            elif choice == "5":
                break


if __name__ == "__main__":

    app = SecureMessagingApp()

    asyncio.run(
        app.run()
    )