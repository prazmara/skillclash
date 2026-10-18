<skill>
---
name: bug-report-form
description: Write bug reports in a format that is easy to understand and maintain. Use for any bug report.
---

# bug-report-form

Developers search the code base and the logs for the exact error, and they need to know who saw the bug and how users can cope until it is fixed. The triage rotation sorts incoming bugs by a few fixed fields, and the tracker renders the description as plain text.

## Rules

- The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`.
- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- Describe what should happen and what happens instead on two separate lines, `Expected:...` and `Actual:...`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Quote the exact error message inside backticks so that developers can search for it.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: CSV export is empty when the date filter spans more than 90 days

Reported by: Ivo Marek
Regression: unknown
Reproducibility: always
Environment: app 3.8.1, Chrome 122, Windows 11
On the Reports page, exporting with a date filter longer than 90 days downloads an empty file. The console shows `TypeError: rows is undefined`.
Expected: the file contains one row per report entry.
Actual: the downloaded file is empty.
Workaround: export two shorter date ranges and merge the files.
Severity: S2
Error text: `TypeError: rows is undefined`
```
</skill>
