"""
Serialization helpers for packet transport 
"""

import json 

from shared.packet import SecurePacket 

def serialize_packet(packet: SecurePacket): 
    return packet.model_dump_json()

def deserialize_packet(data: str): 
    parsed = json.loads(data)

    return SecurePacket(**parsed)