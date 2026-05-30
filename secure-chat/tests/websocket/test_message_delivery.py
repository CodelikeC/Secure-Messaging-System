from fastapi.testclient import TestClient

from server.main import app


client = TestClient(app)


def test_message_delivery():

    with client.websocket_connect(
        "/ws/alice"
    ) as alice:

        with client.websocket_connect(
            "/ws/bob"
        ) as bob:

            packet = {

                "sender": "alice",

                "receiver": "bob",

                "ciphertext": "encrypted",

                "nonce": "nonce123",

                "signature": "signature",

                "timestamp": 9999999999
            }

            alice.send_json(
                packet
            )

            received = (
                bob.receive_json()
            )

            assert (
                received["sender"]
                == "alice"
            )