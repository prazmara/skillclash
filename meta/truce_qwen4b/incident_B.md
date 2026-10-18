---
name: postmortem-lite+incident-brief
description: Merged skill that replaces `postmortem-lite` and `incident-brief`. Use for any incident report.
---

# Merged skill: postmortem-lite + incident-brief

This skill replaces `postmortem-lite` and `incident-brief`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `postmortem-lite`

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.

## Rules kept unchanged from `incident-brief`

- Use at most five bullet points in the whole report.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`. Status: investigating.
- Root cause: [insert the root cause here]. Impact: [describe the user impact here].

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors  
Detection: Synthetic checkout probe detected 500 errors at 09:14 UTC  
Duration: 42 min  
Root cause: TLS certificate on the payments gateway expired, causing the API to fail SSL handshake  
Impact: Users unable to complete purchases; 12,000+ failed transactions during the incident  
Action items:  
- Renew TLS certificate on payments gateway (owner: Security Team)  
- Implement automated certificate expiry alerts (owner: DevOps Team)  
- Review synthetic monitoring thresholds for API health (owner: SRE Team)
```
