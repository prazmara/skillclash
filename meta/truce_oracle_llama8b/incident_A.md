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

- To satisfy both rules, write the report in the following format: - Use at most five bullet points in the main content of the report, and - End with a line `Action items: (owner: <team>)` followed by at least three bullets, each naming an owner as `(owner: <team>)`.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors

Incident ID: INC-2291
Date: 2026-02-11
Time: 09:14 - 09:56 UTC
Duration: 42 min

Impact: Users were unable to complete checkout transactions, resulting in lost sales and potential revenue.

Status: resolved

Root cause: The TLS certificate on the payments gateway expired.

Detection: The synthetic checkout probe detected the issue at 09:14 UTC.

Action items: (owner: DevOps)
• Renew the TLS certificate on the payments gateway (owner: DevOps)
• Implement automated certificate renewal process (owner: DevOps)
• Review and update monitoring to detect similar issues (owner: Monitoring team)
```
