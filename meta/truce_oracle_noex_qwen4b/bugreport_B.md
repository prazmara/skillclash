---
name: bug-dev-handoff+bug-triage-form
description: Merged skill that replaces `bug-dev-handoff` and `bug-triage-form`. Use for any bug report.
---

# Merged skill: bug-dev-handoff + bug-triage-form

This skill replaces `bug-dev-handoff` and `bug-triage-form`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `bug-dev-handoff`

- The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Name the person who found the bug on a line `Reported by: <full name>`.
- Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.

## Rules kept unchanged from `bug-triage-form`

- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.
- Give the app version and the platform on one line that starts with `Environment: `.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Quote the exact error message inside backticks so that developers can search for it. Error text: `Error text:`
