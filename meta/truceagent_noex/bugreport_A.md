---
name: bug-triage-form+bug-dev-handoff
description: Merged skill that replaces `bug-triage-form` and `bug-dev-handoff`. Use for any bug report.
---

# Merged skill: bug-triage-form + bug-dev-handoff

This skill replaces `bug-triage-form` and `bug-dev-handoff`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `bug-triage-form`

- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- The first line must be plain text of the form `Title: <one-line summary>`.
- Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.

## Rules kept unchanged from `bug-dev-handoff`

- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Quote the exact error message inside backticks only on a final line that starts with `Error text:`, for example Error text: `TypeError: rows is undefined`. Keep the rest of the description free of code formatting, so mention the error anywhere else in plain words without backticks.
