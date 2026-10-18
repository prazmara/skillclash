---
name: bug-triage-form
description: Write bug reports in the triage form of the issue tracker. Use for any bug report.
---

# bug-triage-form

The triage rotation sorts incoming bugs by a few fixed fields, and the tracker renders the description as plain text.

## Rules

- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- The first line must be plain text of the form `Title: <one-line summary>`.
- Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.
- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Quote the exact error message inside backticks so that developers can search for it.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
Title: CSV export is empty when the date filter spans more than 90 days

Reported by: Ivo Marek
Reproducibility: always
Severity: S2
Environment: app 3.8.1, Chrome 122, Windows 11
Expected: the file contains one row per report entry.
Actual: the downloaded file is empty and the console shows a TypeError.
Workaround: export two shorter date ranges and merge the files.
```
