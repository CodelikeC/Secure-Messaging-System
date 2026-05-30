from shared.packet import (
    SecurePacket
)

from shared.serialization import (
    serialize_packet,
    deserialize_packet
)


def test_serialization():

    packet = SecurePacket(
        protocol_version="1.0",
        sender="alice",
        receiver="bob",
        timestamp=123,
        nonce="abc",
        ephemeral_public_key="key",
        ciphertext="cipher",
        signature="sig"
    )

    serialized = (
        serialize_packet(
            packet
        )
    )

    restored = (
        deserialize_packet(
            serialized
        )
    )

    assert (
        restored.sender
        == "alice"
    )