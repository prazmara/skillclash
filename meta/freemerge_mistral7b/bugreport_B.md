<skill>
---
name: bug-report
description: Write bug reports that can be easily understood by developers and issue trackers. Use for any bug report.
---

# bug-report

Developers search the code base and the logs for the exact error, and they need to know who saw the bug and how users can cope until it is fixed. The issue tracker renders the description as plain text.

## Rules

- Keep the description free of code formatting, except for the final line that starts with `Error text:`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- The first line must be plain text of the form `Title: <one-line summary>`.
- Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.
- If the bug was previously working, say so on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Quote the exact error message inside backticks so that developers can search for it.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
Title: CSV export is empty when the date filter spans more than 90 days

Severity: S2
Environment: app 3.8.1, Chrome 122, Windows 11
Reproducibility: always
Regression: unknown
Steps:
1. Open the Reports page.
2. Set the date filter to a range longer than 90 days.
3. Click Export CSV.
Expected: the file contains one row per report entry.
Actual: the downloaded file is empty and the console shows `TypeError: rows is undefined`.
Workaround: export two shorter date ranges and merge the files.
Error text: `TypeError: rows is undefined`
```
</skill>
