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

## Rules kept unchanged from `bug-triage-form`

- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Quote the exact error message inside backticks, but only include backticks on a final line that starts with `Error text:`. Keep the description free of code formatting; use backticks only on that final labeled line.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: CSV export produces empty file when date filter spans more than 90 days

Reported by: Ivo Marek  
Regression: unknown  
Expected: Exporting CSV on the Reports page with a date filter over 90 days should generate a file containing the filtered report data.  
Actual: The exported CSV file is empty when the date filter spans more than 90 days.  
Workaround: Export data in smaller date ranges (90 days or less).  
Reproducibility: always  
Environment: App version 3.8.1, Chrome 122 on Windows 11  
Severity: S2  
Error text: `TypeError: rows is undefined`
```
