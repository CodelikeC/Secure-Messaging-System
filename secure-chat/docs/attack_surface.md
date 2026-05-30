# Attack Surface Analysis

## Authentication API

Endpoints:

/auth/register
/auth/login

Risks:

- credential stuffing
- brute force attacks

Future Mitigations:

- rate limiting
- CAPTCHA
- account lockout

---

## WebSocket Interface

Risks:

- malformed packets
- replay attacks

Mitigations:

- schema validation
- nonce cache

---

## Local Storage

Risks:

- stolen database

Mitigations:

- AES encryption
- Argon2id