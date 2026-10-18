---
name: incident-brief+postmortem-lite
description: Merged skill that replaces `incident-brief` and `postmortem-lite`. Use for any incident report.
---

# Merged skill: incident-brief + postmortem-lite

This skill replaces `incident-brief` and `postmortem-lite`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `incident-brief`

- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.

## Rules kept unchanged from `postmortem-lite`

- Say how the problem was noticed on a line that starts with `Detection: `.
- Name the cause on a line that starts with `Root cause: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Describe user impact on a line that starts with `Impact: `. Write impersonally, without using the words `we`, `our`, `us`, or `I`.
- Use at most five bullet points in the whole report, ensuring that the final section is labeled `Action items:` and contains at least three bullets, each naming an owner as `(owner: <team>)`. This section counts toward the five-bullet limit.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors  
Duration: 42 min  
Status: resolved  
Detection: Synthetic checkout probe detected HTTP 500 errors  
Impact: Users were unable to complete purchases during the incident window  
Root cause: TLS certificate on the payments gateway expired  

Action items:  
- Rotate and automate renewal for all TLS certificates in critical paths (owner: Infra)  
- Implement monitoring for certificate expiration dates with 30-day alerts (owner: SRE)  
- Review synthetic probe coverage for dependency services (owner: QA)
```
