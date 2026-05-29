"""
shared constants used across client and server 
"""

# packet validation 

MAX_PACKET_AGE_SECONDS = 60 

# cryptography 

AES_KEY_SIZE = 32 
AES_NONCE_SIZE = 12 

# Session 
SESSION_TIMEOUT_SECONDS = 3600 

# Replay protection 
NONCE_CACHE_SIZE = 10000 
# Protocol 
PROTOCOL_VERSION = "1.0" 

# WebSocket 
WS_HEARTBEAT_INTERVAL = 30