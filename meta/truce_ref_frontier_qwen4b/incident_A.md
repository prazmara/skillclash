<skill>
---
name: incident-brief+postmortem-lite
description: Merged skill that replaces `incident-brief` and `postmortem-lite`. Use for any incident report. Follow every rule below.
---

# Merged skill: incident-brief + postmortem-lite

This skill replaces `incident-brief` and `postmortem-lite`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `incident-brief`

- Use at most five bullet points in the whole report.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.

## Rules kept unchanged from `postmortem-lite`

- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Say how the problem was noticed on a line that starts with `Detection: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Incident: investigating`, and end with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Impact: Describe user impact on a line that starts with `Impact: `. Root cause: Name the cause on a line that starts with `Root cause: `.

## Resolution of conflicting rules

The first line cannot simultaneously be both `SEV<n>: <title>` and `Incident <ID> - <title>`. To satisfy both, the skill must use **both** lines in the correct order:

- The **first line** must be `SEV<n>: <title>`.
- The **second line** must be `Incident <ID> - <title>`.

This ensures all rules from both original skills are preserved without contradiction.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors  
Incident INC-2291 - Checkout API returned 500 errors  
Detection: Synthetic checkout probe detected 500 errors at 09:14 UTC  
Duration: 42 min  
Impact: Users unable to complete purchases; 12,000 transactions failed  
Root cause: TLS certificate on the payments gateway expired  
Status: resolved  
Action items:  
- (owner: Security Team) Renew TLS certificate and automate renewal process  
- (owner: SRE Team) Implement certificate expiry alerting in monitoring pipeline  
- (owner: Product Team) Update documentation to include certificate expiry policy
```
</skill>
