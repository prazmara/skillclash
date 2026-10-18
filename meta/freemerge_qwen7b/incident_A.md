<skill>
---
name: combined-report
description: Write short incident reports for the status channel and blameless postmortem summaries with follow-up actions. Use for any incident report or postmortem.
---

# combined-report

This skill combines the functionality of writing short incident reports for the status channel and blameless postmortem summaries with follow-up actions.

## Rules

- Describe user impact on a line that starts with `Impact: `.
- Use at most five bullet points in the whole report.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.
- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Name the cause on a line that starts with `Root cause: `.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
Incident INC-2291 - Checkout API returned 500 errors

Impact: customers could not complete checkout.
Duration: 42 min
Root cause: the TLS certificate on the payments gateway expired.
Detection: the synthetic checkout probe alerted the on-call engineer.

Action items:
- Add certificate expiry monitoring (owner: platform team)
- Automate certificate renewal (owner: payments team)
- Add a runbook entry for certificate failures (owner: SRE)
- Review alert routing for gateway errors (owner: SRE)
- Audit all certificates expiring this quarter (owner: security team)
- Schedule a follow-up review (owner: incident manager)

Status: resolved
```
</skill>
