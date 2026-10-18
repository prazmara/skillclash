---
name: postmortem-combined
description: Write complete, blameless postmortem summaries with impact, timeline, and follow-up actions. Combines detailed analysis with concise status reporting.
---

# postmortem-combined

A postmortem must clearly communicate impact, timeline, cause, and required follow-up actions. This format serves both detailed review and status channel needs.

## Rules

- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Immediately after the title, include a severity line in the format `SEV<n>: <title>`, derived from the incident ID or context.
- Describe user impact on a line that starts with `Impact: `.
- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- Name the cause on a line that starts with `Root cause: `.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Use at most five bullet points in the whole report unless in the Action items section, which may have more.
- The `Timeline:` line (if present) must clearly state when the incident began and ended using `HH:MM UTC`.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
Incident INC-2291 - Checkout API returned 500 errors
SEV2: Checkout API returned 500 errors

Impact: customers could not complete checkout.
Duration: 42 min
Timeline: errors began at 09:14 UTC and ended at 09:56 UTC after the certificate was renewed.
Detection: the synthetic checkout probe alerted the on-call engineer.
Root cause: the TLS certificate on the payments gateway expired.
Status: resolved

Action items:
- Add certificate expiry monitoring (owner: platform team)
- Automate certificate renewal (owner: payments team)
- Add a runbook entry for certificate failures (owner: SRE)
- Review alert routing for gateway errors (owner: SRE)
- Audit all certificates expiring this quarter (owner: security team)
- Schedule a follow-up review (owner: incident manager)
```
