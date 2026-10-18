---
name: incident-brief+postmortem-lite
description: Merged skill that replaces `incident-brief` and `postmortem-lite`. Use for any incident report.
---

# Merged skill: incident-brief + postmortem-lite

This skill replaces `incident-brief` and `postmortem-lite`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `incident-brief`

- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.
- Describe user impact on a line that starts with `Impact: `.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- State the length of the incident on a line `Duration: <n> min`.

## Rules kept unchanged from `postmortem-lite`

- Name the cause on a line that starts with `Root cause: `.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Write impersonally. Never use the words `we`, `our`, `us` or `I`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Use at most five bullet points in the whole report and end with the line `Action items:` followed by at least three bullets, each named as `(owner: <team>)`.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors

Impact: Users were unable to complete purchases via the checkout API.

Detection: The incident was detected by the synthetic checkout probe.

Root cause: The TLS certificate on the payments gateway expired.

Status: resolved

Duration: 42 min

Action items:
- Update the TLS certificate on the payments gateway (owner: Infrastructure Team)
- Review certificate renewal processes (owner: Security Team)
- Notify stakeholders about the incident (owner: Customer Support Team)
```
