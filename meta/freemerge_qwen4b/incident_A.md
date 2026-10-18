---
name: incident-brief-and-postmortem
description: Write short incident reports or blameless postmortem summaries with follow-up actions. Use for any incident report or postmortem. When both rules apply, the `incident-brief` rules take precedence over `postmortem-lite` rules for conflict resolution.

# incident-brief-and-postmortem

Status-channel readers need the severity, the impact, and the current state in a few lines. For postmortems, include root cause and action items with owners. When rules conflict, the `incident-brief` rules prevail.

## Rules

- Describe user impact on a line that starts with `Impact: `.
- Use at most five bullet points in the whole report.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.
- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Name the cause on a line that starts with `Root cause: `.

## Conflict Resolution

Where two rules cannot both hold, the rule from `incident-brief` wins. For example:
- If both `Impact:` and `Detection:` are required, `Impact:` takes precedence in formatting and placement.
- If both `Duration:` and `Status:` are required, `Status:` must be included and must follow the `Duration:` line.
- If both `SEV<n>:` and `Incident <ID> -` are required, `SEV<n>:` is used as the first line.
- If both `Action items:` and bullet limits are in conflict, the five-bullet limit from `incident-brief` applies.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors

Impact: customers could not complete checkout.
Duration: 42 min
Timeline: errors began at 09:14 UTC and ended at 09:56 UTC after the certificate was renewed.
Status: resolved
Root cause: the TLS certificate on the payments gateway expired.
Detection: the synthetic checkout probe alerted the on-call engineer.

Action items:
- Add certificate expiry monitoring (owner: platform team)
- Automate certificate renewal (owner: payments team)
- Add a runbook entry for certificate failures (owner: SRE)
```
