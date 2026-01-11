# Secure Programming – Honeypot

This application contains a minimal, isolated honeypot mechanism.

## Important rules:
- The honeypot must never expose real data.
- The honeypot must never allow access.
- Logging is observational only.
- Core application code quality must remain high.

The honeypot code must not be used as justification for ignoring static analysis or clean code issues in the core application.

This task is about understanding attacker behaviour, not about exploitation.

## IMPORTANT SECURITY NOTICE

**DO NOT DEPLOY THIS HONEYPOT TO THE PUBLIC INTERNET.**

This is an educational exercise for a controlled lab environment only.

- Run ONLY on localhost (`127.0.0.1`) or isolated VM
- Never expose port 5000 to external networks
- Never deploy on cloud services (AWS, Azure, DigitalOcean, etc.)

---

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt