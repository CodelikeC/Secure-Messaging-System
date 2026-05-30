from client.crypto.key_exchange import (
    KeyExchange
)


def test_handshake():

    alice_private, alice_public = (
        KeyExchange.generate_keypair()
    )

    bob_private, bob_public = (
        KeyExchange.generate_keypair()
    )

    assert (
        KeyExchange.derive_shared_secret(
            alice_private,
            bob_public
        )
        ==
        KeyExchange.derive_shared_secret(
            bob_private,
            alice_public
        )
    )