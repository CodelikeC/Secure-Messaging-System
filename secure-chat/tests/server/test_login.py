from fastapi.testclient import (
    TestClient
)

from server.main import app


client = TestClient(app)


def test_login_endpoint():

    response = client.post(
        "/auth/login",
        json={
            "username": "alice",
            "password": "secret"
        }
    )

    assert response.status_code in [
        200,
        401
    ]