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

- Quote the exact error message inside backticks and place them on a final line that starts with `Error text:`, keeping the rest of the description free of code formatting.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: CSV export on Reports page produces empty file for date filters spanning over 90 days

Regression: unknown

Workaround: none

Expected: A CSV file containing data filtered within the specified date range is generated.

Actual: An empty CSV file is generated.

Severity: S3

Reproducibility: always

Environment: App version 3.8.1, Chrome 122 on Windows 11

Error text: `rows is undefined`
```
