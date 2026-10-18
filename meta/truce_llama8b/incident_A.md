---
name: incident-brief+postmortem-lite
description: Merged skill that replaces `incident-brief` and `postmortem-lite`. Use for any incident report.
---

# Merged skill: incident-brief + postmortem-lite

This skill replaces `incident-brief` and `postmortem-lite`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `incident-brief`

- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.

## Rules kept unchanged from `postmortem-lite`

- Name the cause on a line that starts with `Root cause: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Report the incident duration on a line `Duration: <n> min` followed by a blank line.
- To satisfy both rules, write the report in the following format: - Use at most five bullet points in the main content of the report, and - End with a line `Action items: (owner: <team>)` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Impact: Describe user impact on a line that starts with `Impact: `. Detection: Say how the problem was noticed on a line that starts with `Detection: `. Combined Rule: Write a report where the user impact is described on a line starting with `Impact: `, and the problem detection is described on a line starting with `Detection: `, in that order.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors

Status: resolved

2026-02-11 09:14 UTC - 2026-02-11 09:56 UTC

Duration: 42 min

Impact: Users were unable to complete checkout transactions, resulting in lost sales and potential revenue.

Detection: The synthetic checkout probe alerted the team to the issue.

Root cause: The TLS certificate on the payments gateway expired.

Action items: (owner: DevOps)
- Renew the TLS certificate on the payments gateway (owner: DevOps)
- Update the synthetic checkout probe to monitor for certificate expiration (owner: QA)
- Review and update the certificate renewal process to prevent future expirations (owner: Ops)
```
