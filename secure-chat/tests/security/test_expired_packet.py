import time

from shared.protocol import (
    validate_timestamp
)


def test_expired_packet():

    old_timestamp = (
        int(time.time()) - 3600
    )

    assert (
        validate_timestamp(
            old_timestamp
        )
        is False
    )