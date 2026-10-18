---
name: incident-brief+postmortem-lite
description: Merged skill that replaces `incident-brief` and `postmortem-lite`. Use for any incident report.
---

# Merged skill: incident-brief + postmortem-lite

This skill replaces `incident-brief` and `postmortem-lite`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `incident-brief`

- Use at most five bullet points in the whole report
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`

## Rules kept unchanged from `postmortem-lite`

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- Name the cause on a line that starts with `Root cause: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: `Impact: <user impact> Incident <ID> - <title>` Where: - `<user impact>` is a concise description of the user impact. - `<ID>` is a unique identifier for the incident. - `<title>` is a brief, descriptive title for the incident.
- Write the output in the format: "Detection: 09:14 UTC" to satisfy both rules, where "Detection:" indicates the problem's detection time and "09:14 UTC" is the precise time in 24-hour format.
- Write output as follows: "Incident Duration: <n> min" (where <n> is the number of minutes the incident lasted)
