# Secure Messaging Protocol

## Overview

The Secure Messaging Protocol defines how clients:

- authenticate
- establish secure sessions
- exchange encrypted messages
- verify identities

The protocol is designed around:

- End-to-End Encryption
- Forward Secrecy
- Replay Resistance

---

## Session Establishment

1. Alice obtains Bob's public key
2. Alice generates ephemeral X25519 keypair
3. Bob generates ephemeral X25519 keypair
4. Shared secret is derived using ECDH
5. HKDF derives AES session key

---

## Message Flow

Sender
↓
Encrypt
↓
Sign
↓
Relay Server
↓
Verify
↓
Decrypt
↓
Recipient

---

## Packet Structure

{
    "sender": "alice",
    "receiver": "bob",
    "timestamp": 1717000000,
    "nonce": "...",
    "ephemeral_public_key": "...",
    "ciphertext": "...",
    "signature": "..."
}

---

## Security Properties

- Confidentiality
- Integrity
- Authenticity
- Forward Secrecy
- Replay Protection