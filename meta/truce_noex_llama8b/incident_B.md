---
name: postmortem-lite+incident-brief
description: Merged skill that replaces `postmortem-lite` and `incident-brief`. Use for any incident report.
---

# Merged skill: postmortem-lite + incident-brief

This skill replaces `postmortem-lite` and `incident-brief`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `postmortem-lite`

- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Name the cause on a line that starts with `Root cause: `.

## Rules kept unchanged from `incident-brief`


## Reconciled rules (each one satisfies a rule of both skills at once)

- State the length of the incident on a line `Duration: <n> min` followed by a blank line, then report how long the incident lasted as `Duration: <n> min` on its own line.
- Status: resolved. The postmortem report should be written in a neutral tone, avoiding first-person pronouns such as "we", "our", "us", or "I", and should be structured to provide a clear current state on a single line.
- To satisfy both rules, end the report with a line "Action items:" followed by at least three bullets, each naming an owner as `(owner: <team>)`, and then add a separate line with a title such as "Incident Summary" or "Key Takeaways" followed by at most five bullet points summarizing the incident.
- Detection: Describe the issue that triggered the postmortem-lite analysis, and Impact: Explain how the problem affected the user, including any resulting downtime or data loss.
