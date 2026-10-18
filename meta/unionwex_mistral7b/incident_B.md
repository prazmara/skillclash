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
Incident INC-2291 - Checkout API returned 500 errors
Impact: The Checkout API is experiencing issues, causing some users to encounter errors during the checkout process.

Detection: 09:14 UTC - Unexpected system error occurred in the Checkout API

Incident Brief: Duration: 42 min

Status: investigating
Action items:
- (owner: DevOps) - Investigate the root cause of the TLS certificate expiration
- (owner: SRE) - Implement a monitoring solution to detect certificate expirations in advance
- (owner: Security) - Renew the TLS certificate for the payments gateway and ensure proper renewal procedures are in place
```
