from shared.security import (
    generate_nonce
)


def test_nonce_uniqueness():

    nonce1 = generate_nonce()

    nonce2 = generate_nonce()

    assert nonce1 != nonce2