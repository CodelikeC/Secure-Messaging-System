from fastapi.testclient import (
    TestClient
)

from server.main import app


client = TestClient(app)


def test_register():

    response = client.post(
        "/auth/register",
        json={
            "username": "alice",
            "password": "secret",
            "public_key": "pubkey"
        }
    )

    assert response.status_code in [
        200,
        400
    ]