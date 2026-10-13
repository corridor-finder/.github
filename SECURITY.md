# Security Policy

Corridor Finder shows information that people may rely on when moving money. We treat two kinds of problems seriously.

## 1. Security vulnerabilities

Examples: injection, authentication or authorization flaws, secrets exposed in a repository, server-side request forgery in our anchor verifiers, a vulnerable dependency we actually use.

**Report privately.** Do not open a public issue. In the affected repository open the **Security** tab and choose **Report a vulnerability** (GitHub private vulnerability reporting). If that option is not available there, open a minimal public issue that says only "security contact requested", with no details, and a maintainer will arrange a private channel.

Please include what you found, how to reproduce it, and the impact you expect. We aim to acknowledge reports within 5 working days. We have no bug bounty.

## 2. Data that could mislead users

Examples: a record claiming an anchor serves a country it does not, an invented fee or limit, a source that does not say what the record says, a stale record presented as current.

These are **public bugs**. Open a "Data correction" issue in `corridor-finder-registry` with the record id and the evidence. Corrections to wrong data are fast-tracked.

If you believe an anchor in our data is fraudulent or unsafe, report that to the relevant authorities and tell us through the data-correction issue so we can remove or flag it.

## Scope notes

- Corridor Finder does not hold funds, keys or user accounts. It does not execute payments.
- The planned Soroban contract (attestation of dataset hashes) is testnet-only until it has had an independent review.
- Supported versions: only the latest `main` of each repository.
