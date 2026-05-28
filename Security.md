# Security Policy

## Supported Versions

The following versions currently receive security updates:

| Version | Supported |
| ------- | --------- |
| 1.x     | Yes       |
| < 1.0   | No        |

---

# Security Philosophy

This project follows a Zero-Trust security model.

Core principles include:

* End-to-End Encryption (E2EE)
* Forward Secrecy
* Secure-by-Default design
* Least Privilege
* Defense in Depth

The relay server must never gain access to plaintext messages or session keys.

---

# Supported Cryptography

Approved cryptographic primitives:

| Purpose      | Algorithm   |
| ------------ | ----------- |
| Key Exchange | X25519      |
| Signatures   | Ed25519     |
| Encryption   | AES-256-GCM |
| Password KDF | Argon2id    |
| Randomness   | OS CSPRNG   |

---

# Reporting a Vulnerability

If you discover a security vulnerability:

1. DO NOT publicly disclose the issue immediately.
2. Contact the maintainers privately.
3. Provide:

   * detailed description
   * reproduction steps
   * affected components
   * proof-of-concept if available

---

# Responsible Disclosure Timeline

| Phase                   | Target              |
| ----------------------- | ------------------- |
| Initial acknowledgement | 72 hours            |
| Investigation           | 7 days              |
| Patch preparation       | depends on severity |
| Public disclosure       | after remediation   |

---

# Out-of-Scope Issues

The following are generally considered out of scope:

* denial-of-service from unrealistic traffic volumes
* attacks requiring physical compromise of trusted endpoints
* outdated unsupported versions
* user-generated weak passwords

---

# Known Security Assumptions

The system assumes:

* client devices are trusted
* operating systems are uncompromised
* users verify contact identities when required
* private keys are protected locally

If client endpoints are fully compromised, E2EE guarantees may no longer hold.

---

# Security Design Goals

The system is designed to defend against:

| Threat                    | Status              |
| ------------------------- | ------------------- |
| Passive network sniffing  | mitigated           |
| Replay attacks            | mitigated           |
| Message tampering         | mitigated           |
| Server compromise         | mitigated           |
| Identity spoofing         | partially mitigated |
| Advanced endpoint malware | not fully mitigated |

---

# Secure Development Requirements

All contributors must:

* avoid insecure cryptographic implementations
* validate packet integrity
* sanitize untrusted inputs
* avoid secret leakage in logs
* use secure randomness APIs
* avoid nonce reuse

---

# Third-Party Dependencies

Dependencies should be:

* actively maintained
* security-reviewed
* version-pinned when possible

Avoid introducing unnecessary cryptographic libraries.

---

# Security Audit

This project currently includes:

* internal threat modeling
* replay attack analysis
* integrity validation testing
* protocol-level review

The project has NOT yet undergone:

* external penetration testing
* formal cryptographic audit
* production hardening certification

---

# Disclaimer

This project is primarily educational and research-oriented.

It should not be considered production-grade secure infrastructure without independent professional security review.
