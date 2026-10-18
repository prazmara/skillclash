---
name: bug-dev-handoff+bug-triage-form
description: Merged skill that replaces `bug-dev-handoff` and `bug-triage-form`. Use for any bug report.
---

# Merged skill: bug-dev-handoff + bug-triage-form

This skill replaces `bug-dev-handoff` and `bug-triage-form`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `bug-dev-handoff`

- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.

## Rules kept unchanged from `bug-triage-form`

- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the error message enclosed in backticks (``) on a separate line, which starts with `Error text:`, ensuring the rest of the description is free of any code formatting. For example: ``` Description: User reported an issue with the login functionality. Error text: `Error 403: Forbidden` ```
- Write the output in the following format: ``` ## Bug: <summary> Title: <one-line summary> ```
- Write a response that includes both rules in a single output: "Format the response as follows: Expected: `Severity: [Severity level]` Actual: [Detailed description of the issue] For example: Expected: `Severity: S2` Actual: `The app crashes upon launch due to an unhandled exception in the main thread.`"
