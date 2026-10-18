---
name: bug-dev-handoff-triage
description: Write bug reports that developers can pick up without questions and that fit the triage form. Use for any bug report.
---

# bug-dev-handoff-triage

This skill produces bug reports that developers can act on immediately and that fit the triage form. Developers need to know who found the bug, how to reproduce it, what should happen, what actually happens, how often it occurs, the environment, severity, and any workarounds. The report must be clear, complete, and searchable.

## Rules

- The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`.
- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.
- List reproduction steps under a `Steps:` section, as a numbered list.
- Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Quote the exact error message inside backticks so that developers can search for it, on a line that starts with `Error text:`.
- Do not use code formatting except for the error message in backticks on the `Error text:` line.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
## Bug: CSV export is empty when the date filter spans more than 90 days

Reported by: Ivo Marek
Regression: unknown
Reproducibility: always
Environment: app 3.8.1, Chrome 122, Windows 11
Severity: S2
Steps:
1. Open the Reports page.
2. Set the date filter to a range longer than 90 days.
3. Click Export CSV.
Expected: the file contains one row per report entry.
Actual: the downloaded file is empty.
Workaround: export two shorter date ranges and merge the files.
Error text: `TypeError: rows is undefined`
```
