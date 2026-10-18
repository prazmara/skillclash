---
name: postmortem-lite+incident-brief
description: Combined rules of `postmortem-lite` and `incident-brief`. Use for any incident report.
---

# Combined skill: postmortem-lite + incident-brief

Follow every rule below.

## Rules from `postmortem-lite`

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Name the cause on a line that starts with `Root cause: `.

## Rules from `incident-brief`

- Describe user impact on a line that starts with `Impact: `.
- Use at most five bullet points in the whole report.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.

If two rules cannot both hold, the rule from `postmortem-lite` wins.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors  
Detection: Synthetic checkout probe detected 500 errors at 09:14 UTC  
Duration: 42 min  
Root cause: TLS certificate on the payments gateway expired, causing the API to fail SSL handshake  
Impact: Users unable to complete purchases; 12,000+ failed transactions during the incident  
Action items:  
- Renew TLS certificate on payments gateway (owner: Security Team)  
- Implement automated certificate expiry alerts (owner: DevOps Team)  
- Review synthetic monitoring thresholds for API health (owner: SRE Team)
```
