<skill>
---
name: postmortem-lite-incident-brief
description: Write blameless postmortem summaries with follow-up actions, suitable for both incident reports and status channel updates.
---

# postmortem-lite-incident-brief

A postmortem is only useful if it names the cause and assigns follow-up work. Status-channel readers need the severity, the impact and the current state in a few lines.

## Rules

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.
- Describe user impact on a line that starts with `Impact: `.
- Use at most five bullet points in the whole report.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- Report how the problem was noticed on a line that starts with `Detection: `.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Name the cause on a line that starts with `Root cause: `.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors

Impact: customers could not complete checkout.
Duration: 42 min
Timeline: errors began at 09:14 UTC and ended at 09:56 UTC after the certificate was renewed.
Status: resolved
Detection: the synthetic checkout probe alerted the on-call engineer.

Root cause: the TLS certificate on the payments gateway expired.

Action items:
- Add certificate expiry monitoring (owner: platform team)
- Automate certificate renewal (owner: payments team)
- Add a runbook entry for certificate failures (owner: SRE)
- Review alert routing for gateway errors (owner: SRE)
- Audit all certificates expiring this quarter (owner: security team)
- Schedule a follow-up review (owner: incident manager)
```
</skill>
