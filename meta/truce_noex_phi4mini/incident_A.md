---
name: incident-brief+postmortem-lite
description: Merged skill that replaces `incident-brief` and `postmortem-lite`. Use for any incident report.
---

# Merged skill: incident-brief + postmortem-lite

This skill replaces `incident-brief` and `postmortem-lite`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `incident-brief`

- Describe user impact on a line that starts with `Impact: `.
- Use at most five bullet points in the whole report.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.

## Rules kept unchanged from `postmortem-lite`

- Write impersonally
- Add certificate expiry monitoring (owner: platform team)
- Automate certificate renewal (owner: payments team)
- Add a runbook entry for certificate failures (owner: SRE)
- Review alert routing for gateway errors (owner: SRE)
- Audit all certificates expiring this quarter (owner: security team)
- Schedule a follow-up review (owner: incident manager)
