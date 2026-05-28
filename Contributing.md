# Contributing Guide

Thank you for contributing to Secure Messaging System.

This project values:

* secure engineering
* clean architecture
* defensive programming
* responsible cryptography

---

# Development Principles

Contributors should prioritize:

1. Security correctness
2. Code readability
3. Minimal attack surface
4. Defensive validation
5. Explicit threat awareness

---

# Setup

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Branching Strategy

| Branch    | Purpose             |
| --------- | ------------------- |
| main      | stable release      |
| dev       | active integration  |
| feature/* | feature development |
| hotfix/*  | emergency fixes     |

---

# Commit Convention

```text
feat:
fix:
security:
refactor:
docs:
test:
```

Example:

```text
security: add replay protection validation
```

---

# Pull Request Requirements

Each pull request should include:

* clear description
* threat/security implications
* testing evidence
* documentation updates

---

# Security Rules

Contributors MUST NOT:

* hardcode secrets
* commit private keys
* weaken cryptographic defaults
* disable authentication checks
* bypass encryption validation

---

# Cryptographic Standards

Approved primitives:

| Function     | Approved    |
| ------------ | ----------- |
| Key Exchange | X25519      |
| Signature    | Ed25519     |
| Encryption   | AES-256-GCM |
| Password KDF | Argon2id    |

Deprecated or insecure algorithms should not be introduced.

---

# Code Review Focus

Reviewers evaluate:

* cryptographic correctness
* replay resistance
* validation logic
* error handling
* key lifecycle safety
* memory handling

---

# Testing

All security-sensitive code must include:

* unit tests
* negative tests
* malformed packet tests
* replay attack tests

---

# Documentation

Any architectural or protocol change must update:

* README
* architecture docs
* threat model
* risk register

---

# Responsible Disclosure

Do not publicly disclose critical vulnerabilities before maintainers are notified and remediation is prepared.
