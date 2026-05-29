from pydantic import BaseModel
from typing import Optional 

class SecurePacket(BaseModel):
    protocol_version: str 

    sender: str 
    receiver: str 

    timestamp: int 
    nonce: str 

    ephemeral_public_key: str 

    ciphertext: str 

    signature: str 

    sequence_number: Optional[int] = 0 

class ErrorPacket(BaseModel): 
    error: str 
    timestamp: str 

class HandshakePacket(BaseModel):
    sender: str 

    receiver: str 

    ephemeral_public_key: str 

    timstamp: int 

