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

- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`, where the exact error message must be quoted inside backticks so that developers can search for it.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
Title: CSV export produces empty file when date filter exceeds 90 days
Reproducibility: always
Expected: CSV file should contain report data for the selected date range
Actual: CSV file is empty when date filter spans more than 90 days
Environment: App version 3.8.1, Chrome 122 on Windows 11
Severity: S2
Reported by: Ivo Marek
Regression: unknown
Workaround: Limit the date filter to 90 days or fewer to successfully export data
Error text: `TypeError: rows is undefined`
```
