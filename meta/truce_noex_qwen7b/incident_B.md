---
name: postmortem-lite+incident-brief
description: Merged skill that replaces `postmortem-lite` and `incident-brief`. Use for any incident report.
---

# Merged skill: postmortem-lite + incident-brief

This skill replaces `postmortem-lite` and `incident-brief`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `postmortem-lite`

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Name the cause on a line that starts with `Root cause: `.

## Rules kept unchanged from `incident-brief`

- Describe user impact on a line that starts with `Impact: `.
- Use at most five bullet points in the whole report.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.
