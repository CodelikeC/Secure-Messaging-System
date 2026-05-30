from client.crypto.key_exchange import (
    KeyExchange
)


def test_shared_secret():

    alice_private, alice_public = (
        KeyExchange.generate_keypair()
    )

    bob_private, bob_public = (
        KeyExchange.generate_keypair()
    )

    alice_secret = (
        KeyExchange.derive_shared_secret(
            alice_private,
            bob_public
        )
    )

    bob_secret = (
        KeyExchange.derive_shared_secret(
            bob_private,
            alice_public
        )
    )

    assert alice_secret == bob_secret