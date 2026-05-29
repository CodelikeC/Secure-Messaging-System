from client.crypto.key_exchange import KeyExchange
from client.crypto.kdf import KeyDerivation


class SecureSession:

    def __init__(self):

        self.private_key = None
        self.public_key = None

        self.shared_secret = None

        self.session_key = None

    def initialize():

        private_key, public_key = (
            KeyExchange.generate_keypair()
        )

        self.private_key = private_key
        self.public_key = public_key

    def establish(
        self,
        peer_public_key
    ):

        self.shared_secret = (
            KeyExchange.derive_shared_secret(
                self.private_key,
                peer_public_key
            )
        )

        self.session_key = (
            KeyDerivation.derive_session_key(
                self.shared_secret
            )
        )

    def destroy(self):

        self.private_key = None
        self.public_key = None
        self.shared_secret = None
        self.session_key = None