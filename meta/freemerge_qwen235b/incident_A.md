---
name: incident-brief
description: Write short incident reports and postmortem summaries for the status channel. Combines incident briefing and lightweight postmortem requirements.
---

# incident-brief

Status-channel readers need the severity, the impact, the current state, and follow-up actions in a concise, structured format.

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
Root cause: the TLS certificate on the payments gateway expired.
Detection: synthetic checkout probe alerted the on-call engineer.
Status: resolved

Action items:
- Add certificate expiry monitoring (owner: platform team)
- Automate certificate renewal (owner: payments team)
- Add a runbook entry for certificate failures (owner: SRE)
```
