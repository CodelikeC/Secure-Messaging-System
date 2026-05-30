from fastapi.testclient import TestClient

from server.main import app


client = TestClient(app)


def test_missing_sender():

    with client.websocket_connect(
        "/ws/alice"
    ) as websocket:

        websocket.send_json(
            {
                "receiver": "bob"
            }
        )

        response = (
            websocket.receive_json()
        )

        assert (
            "error"
            in response
        )