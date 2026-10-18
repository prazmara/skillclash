---
name: bug-report
description: Write bug reports that are ready for triage and developer handoff. Use for any bug report.
---

# bug-report

This skill combines the requirements of `bug-triage-form` and `bug-dev-handoff` to ensure that bug reports are both triage-friendly and developer-friendly.

## Rules

- The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`.
- The second line must be plain text of the form `Title: <one-line summary>`.
- The third line must be `Severity: S1`, `Severity: S2`, `Severity: S3`, or `Severity: S4`.
- The fourth line must be `Environment: app version, browser version, operating system`.
- The fifth line must be `Reproducibility: always`, `Reproducibility: sometimes`, or `Reproducibility: once`.
- The sixth line must be `Steps:` followed by detailed steps to reproduce the bug.
- The seventh line must be `Expected: ...` and the eighth line must be `Actual: ...`.
- The ninth line must be `Regression: yes`, `Regression: no`, or `Regression: unknown`.
- The tenth line must be `Reported by: <full name>`.
- The eleventh line must be `Workaround: ...` or `Workaround: none` if there is none.
- The twelfth line must contain the exact error message inside backticks so that developers can search for it.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: CSV export is empty when the date filter spans more than 90 days

Title: CSV export is empty when the date filter spans more than 90 days
Severity: S2
Environment: app 3.8.1, Chrome 122, Windows 11
Reproducibility: always
Steps:
1. Open the Reports page.
2. Set the date filter to a range longer than 90 days.
3. Click Export CSV.
Expected: the file contains one row per report entry.
Actual: the downloaded file is empty.
Regression: unknown
Reported by: Ivo Marek
Workaround: export two shorter date ranges and merge the files.
TypeError: rows is undefined
```
