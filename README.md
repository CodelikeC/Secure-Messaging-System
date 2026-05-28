# Secure Messaging System

## Overview

Secure Messaging System is a cross-platform end-to-end encrypted (E2EE) instant messaging platform designed around Zero-Trust security principles.

The system focuses on protecting user privacy, ensuring data integrity, and defending against common communication threats such as:

* Eavesdropping
* Identity spoofing
* Replay attacks
* Message tampering
* Man-in-the-Middle (MitM) attacks
* Server-side compromise

The central server acts strictly as a relay layer and has no ability to decrypt user messages.

---

# Core Features

## End-to-End Encryption (E2EE)

All messages are encrypted on the sender's device and decrypted only on the recipient's device.

---

## Secure Key Exchange

The system uses:

* X25519 Elliptic Curve Diffie-Hellman (ECDH)

to establish secure shared session keys without transmitting them across the network.

---

## Forward Secrecy

Ephemeral session keys are generated for each session to ensure past communications remain secure even if long-term keys are compromised in the future.

---

## Message Integrity & Authenticity

Messages are protected using:

* AES-256-GCM authentication tags
* Ed25519 digital signatures

to prevent tampering and impersonation.

---

## Secure Local Storage

Sensitive local data such as:

* chat history
* contact lists
* cached sessions

are encrypted using AES-256-GCM with keys derived from user passphrases via Argon2id.

---

# Architecture

```text
Client A
    ↓ encrypted packet
Relay Server
    ↓ encrypted packet
Client B
```

The server:

* relays encrypted packets
* stores public keys
* manages authentication

The server cannot:

* decrypt messages
* access session keys
* read plaintext communication

---

# Technology Stack

| Component           | Technology            |
| ------------------- | --------------------- |
| Backend             | FastAPI               |
| Real-time Transport | WebSocket             |
| Cryptography        | cryptography + PyNaCl |
| Database            | SQLite                |
| Authentication      | JWT                   |
| Password KDF        | Argon2id              |
| Encryption          | AES-256-GCM           |
| Signatures          | Ed25519               |
| Key Exchange        | X25519                |

---

# Threat Model

The system is designed to mitigate:

| Threat            | Mitigation              |
| ----------------- | ----------------------- |
| Eavesdropping     | E2EE                    |
| Replay attacks    | nonce + timestamp       |
| Bit-flipping      | AES-GCM authentication  |
| Identity spoofing | Ed25519 signatures      |
| MitM              | key verification        |
| Database theft    | encrypted local storage |
| Server compromise | Zero-Trust design       |

---

# Project Structure

```text
secure-chat/
│
├── client/
├── server/
├── shared/
├── docs/
├── tests/
└── requirements.txt
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-org/secure-chat.git
cd secure-chat
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Server

```bash
cd server
python main.py
```

---

# Running the Client

```bash
cd client
python app.py
```

---

# Security Principles

This project follows:

* Zero-Trust Architecture
* Principle of Least Privilege
* Defense in Depth
* Cryptographic Agility
* Secure-by-Default Engineering

---

# Educational Purpose

This project is intended for:

* academic research
* security engineering education
* cryptographic protocol exploration

It is NOT production-ready and has not undergone a professional external security audit.

---

# License

This project is released under the MIT License.

---

# Acknowledgements

Inspired by modern secure messaging systems and cryptographic research including:

* Signal Protocol
* TLS 1.3
* Noise Protocol Framework
* Zero-Trust security architecture
