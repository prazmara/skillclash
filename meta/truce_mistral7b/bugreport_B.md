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

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: Empty CSV export when date filter spans more than 90 days
Title: CSV export produces empty file for date ranges exceeding 90 days

Reported by: Ivo Marek
Regression: unknown
Workaround: none

Error text: `TypeError: rows is undefined`

Reproducibility: always

App version: 3.8.1
Browser: Chrome 122
OS: Windows 11

Expected: `Severity: S2`
Actual: `The CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. The console shows 'TypeError: rows is undefined'`
```
