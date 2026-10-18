---
name: postmortem-lite+incident-brief
description: Merged skill that replaces `postmortem-lite` and `incident-brief`. Use for any incident report.
---

# Merged skill: postmortem-lite + incident-brief

This skill replaces `postmortem-lite` and `incident-brief`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `postmortem-lite`

- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Name the cause on a line that starts with `Root cause: `.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- Report how long the incident lasted as `Duration: <n> min` on its own line.

## Rules kept unchanged from `incident-brief`

- Describe user impact on a line that starts with `Impact: `.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: 1. (Incident Summary) - Point 1 - Point 2 - Point 3 - Point 4 (if necessary, up to 5 points total) - Action items: - (owner: <team>) - Action 1 - (owner: <team>) - Action 2 - (owner: <team>) - Action 3 (or more, at least 3 actions)

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
Incident INC-2291 - Checkout API returned 500 errors

1. (Incident Summary)
   - Root cause: The TLS certificate on the payments gateway expired.
   - Detection: Detected by the synthetic checkout probe.
   - Impact: Users were unable to complete checkout for 42 minutes.
   - Duration: 42 min
   - Status: resolved

2. (Action items)
   - (owner: DevOps) - Replace the expired TLS certificate on the payments gateway.
   - (owner: QA) - Test the checkout API after the certificate replacement.
   - (owner: SRE) - Review the monitoring and alerting rules for similar incidents.
```
