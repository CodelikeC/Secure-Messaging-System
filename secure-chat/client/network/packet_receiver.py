from shared.protocol import (
    validate_required_fields,
    validate_timestamp
)


class PacketReceiver:

    @staticmethod
    def validate(packet: dict):

        missing = validate_required_fields(
            packet
        )

        if missing:

            return False, (
                f"Missing fields: {missing}"
            )

        if not validate_timestamp(
            packet["timestamp"]
        ):

            return False, (
                "Packet expired"
            )

        return True, "OK"