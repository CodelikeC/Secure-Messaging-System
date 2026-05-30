import time

from shared.security import (
    generate_nonce,
    generate_message_id
)


class PacketSender:

    @staticmethod
    def build_packet(
        sender,
        receiver,
        ciphertext,
        signature,
        ephemeral_public_key
    ):

        return {
            "message_id": generate_message_id(),
            "sender": sender,
            "receiver": receiver,
            "ciphertext": ciphertext,
            "signature": signature,
            "nonce": generate_nonce(),
            "timestamp": int(time.time()),
            "ephemeral_public_key":
                ephemeral_public_key
        }