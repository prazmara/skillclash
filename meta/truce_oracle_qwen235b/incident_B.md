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

- Use at most five bullet points in the whole report, with the final line being `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`. Ensure all action items are included within the five-bullet limit.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
Incident INC-2291 - Checkout API returned 500 errors  
Root cause: Expired TLS certificate on the payments gateway.  
Detection: Synthetic checkout probe alerted on failed transactions.  
Impact: Users unable to complete purchases for the duration of the incident.  
Duration: 42 min  
Status: resolved  
- Outage occurred between 09:14 UTC and 09:56 UTC due to TLS handshake failure with payments gateway.  
- Certificate renewal process was missed despite automated reminders; manual intervention restored service at 09:56 UTC.  
Action items:  
- Implement certificate expiration checks in monitoring system (owner: Infra)  
- Review and strengthen certificate renewal workflows (owner: Security)  
- Add fallback mechanism for critical gateway dependencies (owner: Payments)
```
