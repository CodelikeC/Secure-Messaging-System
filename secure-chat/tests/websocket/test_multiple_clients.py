from fastapi.testclient import TestClient

from server.main import app


client = TestClient(app)


def test_multiple_connections():

    with client.websocket_connect(
        "/ws/user1"
    ):

        with client.websocket_connect(
            "/ws/user2"
        ):

            with client.websocket_connect(
                "/ws/user3"
            ):

                assert True