<skill>
---
name: bug-triage-dev-handoff
description: Write bug reports in a format that combines the triage form of the issue tracker and the information a developer needs to pick up the bug without asking questions. Use for any bug report.
---

# bug-triage-dev-handoff

The triage rotation sorts incoming bugs by a few fixed fields, and developers search the code base and the logs for the exact error. This skill combines the triage form and the information developers need to pick up the bug without asking questions.

## Rules

- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- The first line must be a level-2 Markdown heading of the form `## Bug: <one-line summary>`.
- Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.
- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Quote the exact error message inside backticks so that developers can search for it.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: CSV export is empty when the date filter spans more than 90 days

Severity: S2
Environment: app 3.8.1, Chrome 122, Windows 11
Reproducibility: always
Reported by: Ivo Marek
Regression: unknown
On the Reports page, exporting with a date filter longer than 90 days downloads an empty file. The console shows `TypeError: rows is undefined`.
Expected: the file contains one row per report entry.
Actual: the downloaded file is empty.
Workaround: export two shorter date ranges and merge the files.
```
</skill>
