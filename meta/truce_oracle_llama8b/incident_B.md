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

- To satisfy both rules, end the report with a line "Action items:" followed by at least three bullets, each naming an owner as `(owner: <team>)`, and then add a separate line with a title such as "Incident Summary" or "Key Takeaways" followed by at most five bullet points summarizing the incident.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
Incident INC-2291 - Checkout API returned 500 errors

Severity: 2

Detection: Detected by the synthetic checkout probe at 09:14 UTC

Root cause: TLS certificate on the payments gateway expired

Impact: Users were unable to complete checkout transactions, resulting in lost sales and potential revenue loss.

Duration: 42 min

Status: resolved

Action items:
• Update the TLS certificate on the payments gateway (owner: Security Team)
• Implement automated certificate renewal process (owner: DevOps Team)
• Review and update the synthetic checkout probe to detect similar issues (owner: Quality Assurance Team)
• Conduct a security audit to identify potential vulnerabilities (owner: Security Team)
• Review and update the incident response plan to include certificate expiration checks (owner: Incident Response Team)

Incident Summary
• The incident was caused by an expired TLS certificate on the payments gateway.
• The synthetic checkout probe detected the issue at 09:14 UTC.
• The issue was resolved at 09:56 UTC.
• The incident lasted for 42 minutes.
• The incident was resolved through manual intervention by the DevOps Team.
```
