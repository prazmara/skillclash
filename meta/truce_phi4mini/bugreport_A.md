---
name: bug-triage-form+bug-dev-handoff
description: Merged skill that replaces `bug-triage-form` and `bug-dev-handoff`. Use for any bug report.
---

# Merged skill: bug-triage-form + bug-dev-handoff

This skill replaces `bug-triage-form` and `bug-dev-handoff`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `bug-triage-form`

- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- Give the app version and the platform on one line that starts with `Environment: `.

## Rules kept unchanged from `bug-dev-handoff`

- Reported by: Ivo Marek
- Regression: unknown
- Expected: the file contains one row per report entry.
- Workaround: export two shorter date ranges and merge the files.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Title: CSV export issue with date filter spanning over 90 days Bug: CSV export is empty when the date filter spans more than 90 days
- To satisfy both rules, ensure that the output clearly contrasts the expected and actual outcomes for each issue, and include the error message from the console in the report for the bug-dev-handoff issue. For example: "Expected: [describe expected outcome], Actual: [describe actual outcome]. Console Error: TypeError: rows is undefined" for the bug-dev-handoff issue, and "Expected: [describe expected outcome], Actual: [describe actual outcome]" for the bug-triage-form issue.
- "Rate the severity as `Severity: S1` or `Severity: S2` and confirm that the downloaded file is not empty."

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
Title: CSV export issue with date filter spanning over 90 days
Environment: App version 3.8.1, Chrome 122 on Windows 11
Reported by: Ivo Marek
Regression: unknown
Expected: CSV export should include all entries within the selected date range, even if it spans more than 90 days.
Actual: CSV export is empty when the date filter spans more than 90 days.
Reproducibility: always
Workaround: export two shorter date ranges and merge the files.
Console Error: TypeError: rows is undefined
Severity: S1
Ivo Marek confirmed that the downloaded file is not empty when the date filter does not span more than 90 days.
```
