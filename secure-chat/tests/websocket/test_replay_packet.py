import time

from fastapi.testclient import (
    TestClient
)

from server.main import app


client = TestClient(app)


def test_replay_attack():

    with client.websocket_connect(
        "/ws/alice"
    ) as websocket:

        packet = {

            "sender": "alice",

            "receiver": "bob",

            "ciphertext": "cipher",

            "nonce": "fixed_nonce",

            "signature": "sig",

            "timestamp": int(
                time.time()
            )
        }

        websocket.send_json(
            packet
        )

        websocket.send_json(
            packet
        )

        response = (
            websocket.receive_json()
        )

        assert (
            response["error"]
            == "Replay attack detected"
        )