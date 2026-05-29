"""
Security-related shared helpers 
"""

import secrets 
import hashlib 

def generate_nonce():
    return secrets.token_hex(16)

def generate_message_id(): 
    return secrets.token_hex(32)

def fingerprint_public_key(public_key: str):
    
    digest = hashlib.sha256(
        public_key.encode()
    ).hexdigest()

    return ":".join(
        digest[i:i+2]
        for i in range(0, len(digest), 2)
    )

