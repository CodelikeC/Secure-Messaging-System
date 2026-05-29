from nacl.signing import SigningKey
from nacl.signing import VerifyKey

import base64


class SignatureHandler:

    @staticmethod
    def generate_identity_keys():

        signing_key = SigningKey.generate()

        verify_key = signing_key.verify_key

        return signing_key, verify_key

    @staticmethod
    def signing_key_to_base64(signing_key):

        return base64.b64encode(
            signing_key.encode()
        ).decode()

    @staticmethod
    def verify_key_to_base64(verify_key):

        return base64.b64encode(
            verify_key.encode()
        ).decode()

    @staticmethod
    def load_signing_key(base64_key: str):

        raw = base64.b64decode(base64_key)

        return SigningKey(raw)

    @staticmethod
    def load_verify_key(base64_key: str):

        raw = base64.b64decode(base64_key)

        return VerifyKey(raw)

    @staticmethod
    def sign_message(
        signing_key,
        message: bytes
    ):

        signed = signing_key.sign(message)

        return base64.b64encode(
            signed.signature
        ).decode()

    @staticmethod
    def verify_signature(
        verify_key,
        message: bytes,
        signature: str
    ):

        decoded_signature = base64.b64decode(signature)

        try:

            verify_key.verify(
                message,
                decoded_signature
            )

            return True

        except Exception:
            return False