# Cryptographic Design

## Algorithms

### Key Exchange

X25519

Reason:

- modern
- fast
- widely audited

---

### Encryption

AES-256-GCM

Reason:

- authenticated encryption
- industry standard

---

### Signatures

Ed25519

Reason:

- small signatures
- high performance
- modern security

---

### Password Protection

Argon2id

Reason:

- memory-hard
- resistant to GPU attacks

---

## Key Hierarchy

Identity Key
        ↓
Ephemeral Key
        ↓
ECDH Secret
        ↓
HKDF
        ↓
Session Key

---

## Forward Secrecy

Each session uses:

- new ephemeral keypair
- new derived session key

Compromising one session does not expose previous sessions.