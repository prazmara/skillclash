---
name: incident-brief-postmortem
description: Write short incident reports for the status channel that also work as a blameless postmortem summary with follow-up actions. Use for any incident report or postmortem.
---

# incident-brief-postmortem

This skill merges `incident-brief` and `postmortem-lite` and replaces both. Status-channel readers need the severity, the impact and the current state in a few lines. A postmortem is only useful if it names the cause and assigns follow-up work, so the same report does that too.

Every rule of both skills is kept. Where two rules cannot both hold, `incident-brief` wins.

## Rules

- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`. This is the `incident-brief` rule. It overrides the `postmortem-lite` rule that the first line is `Incident <ID> - <title>`, which is not used. So that the incident ID is not lost, give it on a line `Incident: <ID>` below the first line.
- Describe user impact on a line that starts with `Impact: `.
- State the length of the incident as `Duration: <n> min` on its own line.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- Name the cause on a line that starts with `Root cause: `.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`. Nothing comes after these bullets.
- Use at most five bullet points in the whole report. Together with the previous rule this means three to five action items and no bullets anywhere else in the report.

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors

Incident: INC-2291
Impact: customers could not complete checkout.
Duration: 42 min
Timeline: errors began at 09:14 UTC and ended at 09:56 UTC after the certificate was renewed.
Root cause: the TLS certificate on the payments gateway expired.
Detection: the synthetic checkout probe alerted the on-call engineer.
Status: resolved

Action items:
- Add certificate expiry monitoring (owner: platform team)
- Automate certificate renewal (owner: payments team)
- Add a runbook entry for certificate failures (owner: SRE)
```
