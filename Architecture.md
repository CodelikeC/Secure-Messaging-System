# System Architecture

# Overview

Secure Messaging System uses a Zero-Trust communication architecture where:

* clients perform all cryptographic operations
* the server acts only as a relay
* plaintext messages never leave client devices

---

# High-Level Architecture

```text id="0bl74r"
+-------------+         +----------------+         +-------------+
|  Client A   | <-----> | Relay Server   | <-----> |  Client B   |
+-------------+         +----------------+         +-------------+

        E2EE Payloads Only
```

---

# Architectural Principles

The system follows:

* Zero-Trust Architecture
* End-to-End Encryption
* Defense in Depth
* Secure-by-Default Design
* Minimal Trusted Computing Base

---

# Component Breakdown

## Client Layer

Responsibilities:

* user authentication
* key generation
* encryption/decryption
* signature verification
* local encrypted storage
* session management

The client is the primary trusted component.

---

## Relay Server

Responsibilities:

* user registration
* public key directory
* WebSocket relay
* session coordination
* JWT authentication

The server is explicitly NOT trusted with message confidentiality.

---

## Shared Protocol Layer

Contains:

* packet definitions
* protocol constants
* serialization logic
* replay protection fields

---

# Cryptographic Architecture

# Identity Keys

Each user owns:

```text id="wvv7ei"
Ed25519 private key
Ed25519 public key
```

Purpose:

* identity
* digital signatures
* authenticity

---

# Session Keys

Temporary X25519 keys are generated per session.

```text id="fz8b8u"
Alice eph_private
Bob eph_private
        ↓
ECDH
        ↓
shared_secret
        ↓
HKDF
        ↓
AES session key
```

Purpose:

* forward secrecy
* session isolation

---

# Message Encryption Pipeline

```text id="4jpw7l"
plaintext
    ↓
AES-256-GCM encrypt
    ↓
ciphertext + auth tag
    ↓
Ed25519 signature
    ↓
network transport
```

---

# Local Storage Architecture

Sensitive local data is encrypted before persistence.

Protected data includes:

* chat history
* session metadata
* cached contacts

Encryption flow:

```text id="2n93fu"
user password
    ↓
Argon2id
    ↓
storage key
    ↓
AES-GCM
    ↓
encrypted SQLite
```

---

# Network Architecture

Transport layer:

* WebSocket over TLS

The application layer additionally provides:

* E2EE
* signatures
* replay protection

This creates layered security.

---

# Packet Structure

```json id="jlcj6j"
{
  "sender": "alice",
  "receiver": "bob",
  "timestamp": 1717000000,
  "nonce": "base64",
  "ephemeral_public_key": "base64",
  "ciphertext": "base64",
  "signature": "base64"
}
```

---

# Replay Protection

Replay mitigation uses:

* timestamps
* nonces
* sequence validation

Packets failing replay validation are rejected.

---

# Trust Boundaries

| Component     | Trust Level       |
| ------------- | ----------------- |
| Client device | trusted           |
| Relay server  | untrusted         |
| Internet      | untrusted         |
| Other users   | partially trusted |

---

# Failure Isolation

The architecture attempts to isolate compromise impact:

| Failure                | Isolation                   |
| ---------------------- | --------------------------- |
| Server compromise      | messages remain encrypted   |
| Session key compromise | previous sessions protected |
| Packet tampering       | authentication failure      |
| Database theft         | encrypted local storage     |

---

# Scalability Considerations

The architecture supports future expansion:

* group messaging
* multi-device sync
* distributed relay servers
* post-quantum cryptography
* federated identity

---

# Security Limitations

The system does NOT fully protect against:

* compromised client endpoints
* malicious operating systems
* physical device extraction
* social engineering
* weak user passwords

---

# Future Improvements

Planned future enhancements:

* Double Ratchet protocol
* Secure multi-device synchronization
* Hardware-backed key storage
* Secure enclave integration
* Post-quantum experimentation
