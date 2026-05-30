# Threat Model

## Assets

Protected assets:

- messages
- session keys
- identity keys
- authentication tokens

---

## Adversaries

### Passive Network Observer

Capabilities:

- sniff traffic

Goal:

- read messages

Mitigation:

- AES-GCM encryption

---

### Active Network Attacker

Capabilities:

- modify packets
- inject packets

Mitigation:

- signatures
- authentication tags

---

### Malicious Server

Capabilities:

- access database
- relay packets

Mitigation:

- E2EE
- zero-trust architecture

---

### Replay Attacker

Capabilities:

- resend packets

Mitigation:

- timestamp
- nonce validation

---

## Assumptions

Trusted:

- local cryptographic implementation

Not Trusted:

- internet
- relay server