from fastapi.testclient import TestClient

from server.main import app


client = TestClient(app)


def test_websocket_disconnect():

    websocket = client.websocket_connect(
        "/ws/test_user"
    )

    websocket.close()

    assert True