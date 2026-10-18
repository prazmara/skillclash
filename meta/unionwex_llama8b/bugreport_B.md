---
name: bug-dev-handoff+bug-triage-form
description: Combined rules of `bug-dev-handoff` and `bug-triage-form`. Use for any bug report.
---

# Combined skill: bug-dev-handoff + bug-triage-form

Follow every rule below.

## Rules from `bug-dev-handoff`

- The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`.
- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Quote the exact error message inside backticks so that developers can search for it.

## Rules from `bug-triage-form`

- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- The first line must be plain text of the form `Title: <one-line summary>`.
- Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.

If two rules cannot both hold, the rule from `bug-dev-handoff` wins.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: CSV export fails when date filter spans more than 90 days

Title: CSV export empty when date filter spans more than 90 days

Reported by: Ivo Marek

Regression: unknown

Workaround: none

Environment: App version 3.8.1, Chrome 122 on Windows 11

Severity: S2

Reproducibility: always

Expected: The CSV export to contain data from the selected date range.

Actual: The CSV export is an empty file.

Error text: `TypeError: rows is undefined`
```
