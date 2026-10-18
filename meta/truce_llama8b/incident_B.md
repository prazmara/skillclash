---
name: postmortem-lite+incident-brief
description: Merged skill that replaces `postmortem-lite` and `incident-brief`. Use for any incident report.
---

# Merged skill: postmortem-lite + incident-brief

This skill replaces `postmortem-lite` and `incident-brief`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `postmortem-lite`

- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Name the cause on a line that starts with `Root cause: `.

## Rules kept unchanged from `incident-brief`


## Reconciled rules (each one satisfies a rule of both skills at once)

- State the length of the incident on a line `Duration: <n> min` followed by a blank line, then report how long the incident lasted as `Duration: <n> min` on its own line.
- Status: resolved. The postmortem report should be written in a neutral tone, avoiding first-person pronouns such as "we", "our", "us", or "I", and should be structured to provide a clear current state on a single line.
- To satisfy both rules, end the report with a line "Action items:" followed by at least three bullets, each naming an owner as `(owner: <team>)`, and then add a separate line with a title such as "Incident Summary" or "Key Takeaways" followed by at most five bullet points summarizing the incident.
- Detection: Describe the issue that triggered the postmortem-lite analysis, and Impact: Explain how the problem affected the user, including any resulting downtime or data loss.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
Incident INC-2291 - Checkout API returned 500 errors

Severity: 2

Duration: 42 min

 
Duration: 42 min

Status: resolved

Root cause: TLS certificate on the payments gateway expired

Detection: The synthetic checkout probe triggered the incident analysis at 09:14 UTC on 2026-02-11, detecting 500 errors from the checkout API.

Impact: The expired TLS certificate caused the checkout API to return 500 errors, resulting in downtime for users attempting to complete transactions.

Action items:
• (owner: Payments Team) Renew the TLS certificate on the payments gateway.
• (owner: DevOps Team) Implement automated certificate renewal for the payments gateway.
• (owner: QA Team) Update the synthetic checkout probe to detect certificate expiration issues.
• (owner: DevOps Team) Review and update the incident response plan to include certificate expiration scenarios.
• (owner: Product Team) Investigate alternative payment gateway options with automatic certificate renewal.

Incident Summary
• The incident was detected by the synthetic checkout probe at 09:14 UTC on 2026-02-11.
• The checkout API returned 500 errors due to the expired TLS certificate.
• The incident was resolved at 09:56 UTC on 2026-02-11.
• The root cause was identified as the expired TLS certificate on the payments gateway.
• The incident response plan will be reviewed and updated to include certificate expiration scenarios.
```
