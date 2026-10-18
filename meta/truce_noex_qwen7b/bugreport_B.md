---
name: bug-dev-handoff+bug-triage-form
description: Merged skill that replaces `bug-dev-handoff` and `bug-triage-form`. Use for any bug report.
---

# Merged skill: bug-dev-handoff + bug-triage-form

This skill replaces `bug-dev-handoff` and `bug-triage-form`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `bug-dev-handoff`

- The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`.
- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Quote the exact error message inside backticks so that developers can search for it.

## Rules kept unchanged from `bug-triage-form`

- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.
