from shared.protocol import (
    validate_required_fields
)


def test_required_fields():

    packet = {
        "sender": "alice"
    }

    missing = (
        validate_required_fields(
            packet
        )
    )

    assert len(missing) > 0