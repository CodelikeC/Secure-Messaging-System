from shared.replay_cache import (
    ReplayCache
)


def test_replay_detection():

    cache = ReplayCache()

    nonce = "abc123"

    assert cache.contains(
        nonce
    ) is False

    cache.add(
        nonce
    )

    assert cache.contains(
        nonce
    ) is True