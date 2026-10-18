---
name: bug-triage-form+bug-dev-handoff
description: Merged skill that replaces `bug-triage-form` and `bug-dev-handoff`. Use for any bug report.
---

# Merged skill: bug-triage-form + bug-dev-handoff

This skill replaces `bug-triage-form` and `bug-dev-handoff`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `bug-triage-form`

- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`

## Rules kept unchanged from `bug-dev-handoff`

- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output with the error message quoted and enclosed in backticks if it appears, and ensure the description is free of code formatting, except for the final line that starts with `Error text:`.
- Write the output as follows: ``` ## Bug: <one-line summary> ``` This line should be a level-2 Markdown heading and also serve as the one-line summary for the bug triage form.
- Write the output in the following format: ``` Severity: [Severity Level] Expected: [Describe the expected behavior] Actual: [Describe the current behavior] ``` Replace `[Severity Level]` with S1, S2, S3, or S4, and replace `[Describe the expected behavior]` and `[Describe the current behavior]` with appropriate descriptions. This format will satisfy both rules from `bug-triage-form` and `bug-dev-handoff`.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: CSV export on Reports page produces an empty file for date filters spanning more than 90 days

Severity: S2
Expected: The CSV export should generate a file with data for the specified date range.
Actual: The CSV export generates an empty file when the date filter spans more than 90 days.

Error text:
```
TypeError: rows is undefined
```

Reproducibility: always
Reported by: Ivo Marek
Regression: unknown
Workaround: None

App version: 3.8.1
Browser: Chrome 122
Operating system: Windows 11
