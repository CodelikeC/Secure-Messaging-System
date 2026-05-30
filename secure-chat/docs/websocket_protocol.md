# WebSocket Protocol

Endpoint:

ws://host/ws/{username}

---

## Message Packet

{
    "sender": "...",
    "receiver": "...",
    "ciphertext": "...",
    "nonce": "...",
    "signature": "...",
    "timestamp": ...
}

---

## Heartbeat Packet

{
    "type": "heartbeat",
    "timestamp": ...
}