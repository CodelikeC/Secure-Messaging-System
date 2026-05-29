"""
Protocol utilities and validation helpers...
"""

import time 

from shared.constants import MAX_PACKET_AGE_SECONDS

def validate_timestamp(timestamp: int) -> bool: 
    current_time = int(time.time())

    delta = abs(current_time - timestamp)

    return delta <= MAX_PACKET_AGE_SECONDS 

def validate_required_fields(packet: dict): 
    required_fields = [
        "sender", 
        "receiver", 
        "ciphertext", 
        "nonce", 
        "signature", 
        "timestamp", 
        "ephemal_public_key"
    ]

    missing = []

    for field in required_fields:
        if field not in packet: 
            missing.append(field)
    return missing 

def is_valid_protocol_version(version: str):
    supported_versions = [
        "1.0"
    ]

    return version in supported_versions