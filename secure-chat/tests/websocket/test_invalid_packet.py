from fastapi.testclient import TestClient

from server.main import app


client = TestClient(app)


def test_invalid_packet():

    with client.websocket_connect(
        "/ws/alice"
    ) as websocket:

        websocket.send_json(
            {
                "invalid": True
            }
        )

        response = (
            websocket.receive_json()
        )

        assert (
            "error"
            in response
        )