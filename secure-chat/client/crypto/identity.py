from client.crypto.signatures import SignatureHandler

from shared.security import fingerprint_public_key


class IdentityManager:

    def __init__(self):

        self.signing_key = None
        self.verify_key = None

    def create_identity(self):

        signing_key, verify_key = (
            SignatureHandler.generate_identity_keys()
        )

        self.signing_key = signing_key

        self.verify_key = verify_key

    def export_public_key(self):

        return SignatureHandler.verify_key_to_base64(
            self.verify_key
        )

    def export_private_key(self):

        return SignatureHandler.signing_key_to_base64(
            self.signing_key
        )

    def fingerprint(self):

        return fingerprint_public_key(
            self.export_public_key()
        )