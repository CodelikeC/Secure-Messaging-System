from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey,
    X25519PublicKey
)

from cryptography.hazmat.primitives import serialization

import base64


class KeyExchange:

    @staticmethod
    def generate_keypair():

        private_key = X25519PrivateKey.generate()

        public_key = private_key.public_key()

        return private_key, public_key

    @staticmethod
    def public_key_to_base64(public_key):

        raw = public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )

        return base64.b64encode(raw).decode()

    @staticmethod
    def load_public_key(base64_key: str):

        raw = base64.b64decode(base64_key)

        return X25519PublicKey.from_public_bytes(raw)

    @staticmethod
    def derive_shared_secret(
        private_key,
        peer_public_key
    ):

        return private_key.exchange(peer_public_key)