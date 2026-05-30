from fastapi.testclient import TestClient

from server.main import app


client = TestClient(app)


def test_websocket_connect():

    with client.websocket_connect(
        "/ws/test_user"
    ) as websocket:

        assert websocket is not None