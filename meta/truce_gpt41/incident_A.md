---
name: incident-brief+postmortem-lite
description: Merged skill that replaces `incident-brief` and `postmortem-lite`. Use for any incident report.
---

# Merged skill: incident-brief + postmortem-lite

This skill replaces `incident-brief` and `postmortem-lite`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `incident-brief`

- Describe user impact on a line that starts with `Impact: `.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.

## Rules kept unchanged from `postmortem-lite`

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Name the cause on a line that starts with `Root cause: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The first line must be `SEV<n>: Incident <ID> - <title>`, for example `SEV2: Incident INC-2291 - Checkout API returned 500 errors`. This format satisfies both rules by including all required markers, labels, and structure in a single line.
- Write the whole report using at most five bullet points, and use the last three (or more) bullets after the line `Action items:`, each naming an owner as `(owner: <team>)`.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Incident INC-2291 - Checkout API returned 500 errors

- Impact: Users were unable to complete purchases via the checkout API.
- Detection: Detected by the synthetic checkout probe.
- Root cause: Expired TLS certificate on the payments gateway.
- Duration: 42 min
- Status: resolved

Action items:
- Implement automated TLS certificate expiry monitoring and alerting (owner: SRE)
- Review and update certificate renewal procedures (owner: Payments)
- Conduct a post-incident review to identify process gaps (owner: Engineering)
```
