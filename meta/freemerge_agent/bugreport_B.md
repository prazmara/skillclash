---
name: bug-triage-handoff
description: Write bug reports that a developer can pick up without asking questions and that carry the fields of the tracker's triage form. Use for any bug report.
---

# bug-triage-handoff

This skill merges `bug-triage-form` and `bug-dev-handoff` and replaces both. Developers search the code base and the logs for the exact error, and they need to know who saw the bug and how users can cope until it is fixed. The triage rotation sorts incoming bugs by a few fixed fields, and the tracker renders the description as plain text.

Every rule of both skills is kept. Where two rules cannot both hold, `bug-dev-handoff` wins.

## Rules

- The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`. This is the `bug-dev-handoff` rule. It overrides the `bug-triage-form` rule that the first line is plain text of the form `Title: <one-line summary>`, so no `Title:` line is written.
- Name the person who found the bug on a line `Reported by: <full name>`.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.
- Give the app version and the platform on one line that starts with `Environment: `.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Describe what should happen and what happens instead on two separate lines that start with `Expected: ` and `Actual: `.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- Quote the exact error message inside backticks so that developers can search for it. To satisfy the previous rule as well, the quote goes on the final line of the report, written as `Error text: ` followed by the exact message in backticks. Everywhere else, mention the error in plain words without backticks.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: CSV export is empty when the date filter spans more than 90 days

Reported by: Ivo Marek
Severity: S2
Environment: app 3.8.1, Chrome 122, Windows 11
Reproducibility: always
Regression: unknown
Steps:
1. Open the Reports page.
2. Set the date filter to a range longer than 90 days.
3. Click Export CSV.
Expected: the file contains one row per report entry.
Actual: the downloaded file is empty and the console shows a TypeError.
Workaround: export two shorter date ranges and merge the files.
Error text: `TypeError: rows is undefined`
```
