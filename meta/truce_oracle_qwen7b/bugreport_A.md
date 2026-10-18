---
name: bug-triage-form+bug-dev-handoff
description: Merged skill that replaces `bug-triage-form` and `bug-dev-handoff`. Use for any bug report.
---

# Merged skill: bug-triage-form + bug-dev-handoff

This skill replaces `bug-triage-form` and `bug-dev-handoff`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `bug-triage-form`

- The first line must be plain text of the form `Title: <one-line summary>`.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.
- Give the app version and the platform on one line that starts with `Environment: `.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.

## Rules kept unchanged from `bug-dev-handoff`

- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Name the person who found the bug on a line `Reported by: <full name>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Keep the description free of code formatting and quote the exact error message inside backticks on a final line that starts with `Error text:`.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
Title: CSV export on Reports page produces empty file for date filters > 90 days
Severity: S3
Environment: App version 3.8.1, Chrome 122 on Windows 11
Reproducibility: always
Expected: CSV file should contain data within the specified date range
Actual: CSV file is empty

Regression: unknown
Workaround: none
Reported by: Ivo Marek
Error text: TypeError: rows is undefined
```
