import time

from fastapi.testclient import (
    TestClient
)

from server.main import app


client = TestClient(app)


def test_expired_packet():

    with client.websocket_connect(
        "/ws/alice"
    ) as websocket:

        packet = {

            "sender": "alice",

            "receiver": "bob",

            "ciphertext": "cipher",

            "nonce": "nonce_expired",

            "signature": "sig",

            "timestamp": (
                int(time.time())
                - 3600
            )
        }

        websocket.send_json(
            packet
        )

        response = (
            websocket.receive_json()
        )

        assert (
            response["error"]
            == "Packet expired"
        )