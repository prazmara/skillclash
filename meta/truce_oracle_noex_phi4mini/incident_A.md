---
name: incident-brief+postmortem-lite
description: Merged skill that replaces `incident-brief` and `postmortem-lite`. Use for any incident report.
---

# Merged skill: incident-brief + postmortem-lite

This skill replaces `incident-brief` and `postmortem-lite`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `incident-brief`

- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.
- Describe user impact on a line that starts with `Impact: `.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- State the length of the incident on a line `Duration: <n> min`.

## Rules kept unchanged from `postmortem-lite`

- Name the cause on a line that starts with `Root cause: `.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Write impersonally. Never use the words `we`, `our`, `us` or `I`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Combine the bullet point limit from the `incident-brief` rule with the action items requirement from the `postmortem-lite` rule by creating a concise incident summary with no more than five bullet points, followed by a list of at least three action items, each assigned to a specific team member. End the report with the line `Action items:` and list the action items as `(owner: <team>)`.
