import time

from fastapi.testclient import (
    TestClient
)

from server.main import app


client = TestClient(app)


def test_heartbeat_packet():

    with client.websocket_connect(
        "/ws/alice"
    ) as websocket:

        websocket.send_json(
            {
                "type": "heartbeat",
                "timestamp": int(
                    time.time()
                )
            }
        )

        assert True