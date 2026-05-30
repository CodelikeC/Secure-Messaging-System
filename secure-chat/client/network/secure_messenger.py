from client.crypto.aes import (
    AESHandler
)

from client.crypto.signatures import (
    SignatureHandler
)

from client.network.packet_sender import (
    PacketSender
)


class SecureMessenger:

    @staticmethod
    def create_secure_packet(
        sender,
        receiver,
        plaintext,
        session_key,
        signing_key,
        ephemeral_public_key
    ):

        encrypted = (
            AESHandler.encrypt(
                session_key,
                plaintext
            )
        )

        signature = (
            SignatureHandler.sign_message(
                signing_key,
                encrypted[
                    "ciphertext"
                ].encode()
            )
        )

        return PacketSender.build_packet(
            sender=sender,
            receiver=receiver,
            ciphertext=encrypted[
                "ciphertext"
            ],
            signature=signature,
            ephemeral_public_key=
                ephemeral_public_key
        )