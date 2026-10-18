---
name: incident-brief-postmortem
description: Write concise, blameless incident reports and postmortem summaries for the status channel, including severity, impact, timeline, cause, detection, and follow-up actions.
---

# incident-brief-postmortem

This skill produces short, actionable incident reports and postmortem summaries for the status channel. Reports must include severity, impact, timeline, cause, detection, and follow-up actions, while remaining concise and blameless.

## Rules

- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.
- Describe user impact on a line that starts with `Impact: `.
- Use at most five bullet points in the whole report.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Name the cause on a line that starts with `Root cause: `.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.

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
- Review alert routing for gateway errors (owner: SRE)
- Audit all certificates expiring this quarter (owner: security team)
```
