---
name: postmortem-incident-merged
description: Write blameless postmortem summaries and short incident reports for any incident, including cause, impact, timeline, and follow-up actions.
---

# postmortem-incident-merged

This skill writes incident reports and postmortems that are blameless, concise, and actionable. It includes all required details for both postmortem and status channel audiences.

## Rules

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.
- Name the cause on a line that starts with `Root cause: `.
- Describe user impact on a line that starts with `Impact: `.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- Include a timeline as `Timeline: <summary of key times and actions>`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Use as many bullet points as needed for action items (the five-bullet limit does not apply).
- The rule for the first line from `postmortem-lite` (`Incident <ID> - <title>`) replaces the first line rule from `incident-brief`.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
Incident INC-2291 - Checkout API returned 500 errors

Duration: 42 min
Root cause: the TLS certificate on the payments gateway expired.
Detection: the synthetic checkout probe alerted the on-call engineer.
Impact: customers could not complete checkout.
Timeline: errors began at 09:14 UTC and ended at 09:56 UTC after the certificate was renewed.
Status: resolved

Action items:
- Add certificate expiry monitoring (owner: platform team)
- Automate certificate renewal (owner: payments team)
- Add a runbook entry for certificate failures (owner: SRE)
- Review alert routing for gateway errors (owner: SRE)
- Audit all certificates expiring this quarter (owner: security team)
- Schedule a follow-up review (owner: incident manager)
```
