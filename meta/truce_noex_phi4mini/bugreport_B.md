---
name: bug-dev-handoff+bug-triage-form
description: Merged skill that replaces `bug-dev-handoff` and `bug-triage-form`. Use for any bug report.
---

# Merged skill: bug-dev-handoff + bug-triage-form

This skill replaces `bug-dev-handoff` and `bug-triage-form`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `bug-dev-handoff`

- Reported by: Ivo Marek
- Regression: unknown
- Expected: the file contains one row per report entry.
- Workaround: export two shorter date ranges and merge the files.

## Rules kept unchanged from `bug-triage-form`

- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- Give the app version and the platform on one line that starts with `Environment: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- To satisfy both rules, ensure the CSV export begins with a line formatted as `Title: <one-line summary>` followed by the data, and if the date filter spans more than 90 days, include all relevant data without the export being empty.
- To satisfy both rules, ensure that the output does not include any lines starting with `Expected: ` or `Actual: `, and that the date filter on the Reports page is set to 90 days or less to avoid the `TypeError: rows is undefined` error.
- To satisfy both rules, the output must include a line stating "Severity: S1" or "Severity: S2" or "Severity: S3" or "Severity: S4" and must also indicate that the downloaded file is empty.
