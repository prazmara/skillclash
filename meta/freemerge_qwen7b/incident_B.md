---
name: combined-skill
description: Write concise and detailed incident reports suitable for both postmortems and status updates. Use for any incident report or postmortem.
---

# combined-skill

This skill combines the functionality of writing both concise incident reports for the status channel and detailed postmortem summaries.

## Rules

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- The first line must be `SEV<n>: <title>` for status reports or `Incident <ID> - <title>` for postmortems, for example `SEV2: Checkout API returned 500 errors` or `Incident INC-2291 - Checkout API returned 500 errors`.
- For status reports, describe user impact on a line that starts with `Impact: `.
- For postmortems, say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.
- For status reports, give the current state on a line `Status: resolved`, `Status: monitoring`, or `Status: investigating`.
- For postmortems, end with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Name the cause on a line that starts with `Root cause: ` for postmortems.
- For status reports, state the length of the incident on a line `Duration: <n> min`.
- For postmortems, the first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- For postmortems, the output should include at least three action items.
- For status reports, use at most five bullet points in the whole report.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
Incident INC-2291 - Checkout API returned 500 errors

Detection: the synthetic checkout probe alerted the on-call engineer.
Duration: 42 min
Root cause: the TLS certificate on the payments gateway expired.
Action items:
- Add certificate expiry monitoring (owner: platform team)
- Automate certificate renewal (owner: payments team)
- Add a runbook entry for certificate failures (owner: SRE)
- Review alert routing for gateway errors (owner: SRE)
- Audit all certificates expiring this quarter (owner: security team)
- Schedule a follow-up review (owner: incident manager)
```

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors

Impact: customers could not complete checkout.
Duration: 42 min
Timeline: errors began at 09:14 UTC and ended at 09:56 UTC after the certificate was renewed.
Status: resolved
```
