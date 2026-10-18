---
name: postmortem-lite+incident-brief
description: Merged skill that replaces `postmortem-lite` and `incident-brief`. Use for any incident report.
---

# Merged skill: postmortem-lite + incident-brief

This skill replaces `postmortem-lite` and `incident-brief`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `postmortem-lite`

- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.
- Name the cause on a line that starts with `Root cause: `.

## Rules kept unchanged from `incident-brief`

- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write impersonally, avoiding the words `we`, `our`, `us`, and `I`. Begin a line with `Impact: ` to describe user impact.
- Use at most five bullet points in the whole report, with the final line being `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`. Ensure all action items are included within the five-bullet limit.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
Incident INC-2291 - Checkout API returned 500 errors  
Detection: Synthetic checkout probe detected HTTP 500 errors  
Duration: 42 min  
Root cause: TLS certificate on the payments gateway expired  
Impact: Users unable to complete purchases via the checkout API during the incident period  
Status: resolved  
Action items:  
- Renew and validate TLS certificate for payments gateway (owner: Infra)  
- Implement automated certificate expiration alerts (owner: Security)  
- Update synthetic probe to detect TLS-related failures (owner: SRE)
```
