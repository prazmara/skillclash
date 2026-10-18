---
name: bug-triage-form+bug-dev-handoff
description: Combined rules of `bug-triage-form` and `bug-dev-handoff`. Use for any bug report.
---

# Combined skill: bug-triage-form + bug-dev-handoff

Follow every rule below.

## Rules from `bug-triage-form`

- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- The first line must be plain text of the form `Title: <one-line summary>`.
- Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.

## Rules from `bug-dev-handoff`

- The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`.
- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Quote the exact error message inside backticks so that developers can search for it.

If two rules cannot both hold, the rule from `bug-triage-form` wins.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: CSV export fails when date filter spans more than 90 days

Reported by: Ivo Marek
Regression: unknown
Severity: S3
Reproducibility: always
Environment: App version 3.8.1, Chrome 122 on Windows 11
Expected: A CSV file with data from the filtered date range
Actual: An empty CSV file is produced
Workaround: none
Error text:
TypeError: rows is undefined
```
