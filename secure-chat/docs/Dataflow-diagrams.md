# Data Flow Diagram (DFD)

# Secure Messaging System

## Overview

The Secure Messaging System is designed using a Zero-Trust architecture in which the relay server is considered untrusted. All sensitive data remains encrypted throughout transmission and storage.

---

## Level 0 DFD

```text
+--------+
| Alice  |
+--------+
     |
     | Encrypted Message
     v
+------------------+
| Relay Server     |
| (Untrusted)      |
+------------------+
     |
     | Encrypted Message
     v
+--------+
| Bob    |
+--------+
```

The relay server only forwards ciphertext and never possesses session keys.

---

## Level 1 DFD

### Registration Flow

```text
Alice
  |
  | Username
  | Password
  | Public Key
  v
Authentication API
  |
  v
User Database
```

Stored Data:

* username
* Argon2id password hash
* public verification key

The private key is never transmitted to the server.

---

### Login Flow

```text
Alice
  |
  | Username + Password
  v
Authentication API
  |
  | JWT Token
  v
Alice
```

The server verifies password hashes using Argon2id.

---

### Public Key Retrieval

```text
Alice
  |
  | Request Bob Public Key
  v
Server Database
  |
  | Bob Public Key
  v
Alice
```

Public keys are considered public information.

---

### Secure Session Establishment

```text
Alice
   |
   | Ephemeral Public Key
   v
Bob

Bob
   |
   | Ephemeral Public Key
   v
Alice

Shared Secret
      |
      v
HKDF
      |
      v
AES-256 Session Key
```

Session keys never leave client devices.

---

### Message Transmission

```text
Plaintext
    |
    v
AES-256-GCM Encryption
    |
    v
Ciphertext
    |
    v
Ed25519 Signature
    |
    v
Secure Packet
    |
    v
Relay Server
    |
    v
Recipient
```

The relay server only processes encrypted packets.

---

### Local Storage Flow

```text
Chat History
     |
     v
Argon2id
     |
     v
Storage Key
     |
     v
AES Encryption
     |
     v
Encrypted Storage
```

Compromise of local files does not reveal plaintext messages without the user's password.

---

## Trust Boundaries

### Trusted

* Client cryptographic engine
* User device memory
* Cryptographic libraries

### Untrusted

* Internet
* Relay server
* Network infrastructure
* Wi-Fi access points
* ISPs

---

## Security Objectives

1. Confidentiality
2. Integrity
3. Authenticity
4. Replay Protection
5. Forward Secrecy
6. Server Compromise Resistance

```
```
