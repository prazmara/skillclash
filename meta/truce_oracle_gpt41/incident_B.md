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

- Write the report using at most five bullet points in total, and end with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`. The action item bullets count toward the five-bullet total.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
Incident INC-2291 - Checkout API returned 500 errors

- Root cause: Expired TLS certificate on the payments gateway.
- Detection: Synthetic checkout probe.
- Impact: Users were unable to complete purchases via the checkout API.
- Duration: 42 min (from 09:14 UTC to 09:56 UTC on 2026-02-11)
- Status: resolved

Action items:
- Implement automated TLS certificate expiry monitoring and alerting (owner: SRE)
- Review and update certificate renewal procedures (owner: Payments)
- Conduct a post-incident review to identify process gaps (owner: Engineering)
```
