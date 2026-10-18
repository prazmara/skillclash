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

- Write a report with at most five bullet points in total, including the action items. End the report with the line "Action items:" followed by at least three bullet points, each naming an owner as "(owner: <team>)". For example: ``` - Incident occurred at 10:30 AM - System response was delayed - Root cause identified: Server overload - Corrective action taken: Server capacity increased - Incident resolved at 12:00 PM Action items: - (owner: IT) Monitor server load and capacity - (owner: DevOps) Implement load balancing solution - (owner: Support) Update SLA documentation ```

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors (Incident ID INC-2291)

Impact: Checkout functionality was unavailable for 42 minutes, affecting 12% of active users.

Detection: Detected by the synthetic checkout probe at 09:14 UTC.

Root cause: TLS certificate on the payments gateway expired.

Status: resolved

Duration: 42 min

- Incident occurred at 09:14 UTC
- System response was delayed
- Corrective action taken: TLS certificate on the payments gateway was renewed

Action items:
- (owner: IT) Monitor TLS certificate expiration dates and renew them proactively
- (owner: DevOps) Implement automated certificate renewal system
- (owner: Support) Update incident response documentation to include TLS certificate expiration as a potential cause for API errors.
```
