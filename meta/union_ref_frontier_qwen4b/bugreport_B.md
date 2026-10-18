<skill>
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
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `S3`, or `S4`.

## Conflict Resolution

If two rules cannot both hold, the rule from `bug-dev-handoff` wins **only if** it is directly about the structure of the bug report (e.g., heading, reporter, expected/actual, workaround, error message quoting).  
For rules that are mutually exclusive in form or content (e.g., first line format vs. error message quoting), **both must be satisfied** by adjusting the structure appropriately.  
Specifically:
- The first line **must** be a level-2 Markdown heading (`## Bug: <summary>`) **and** must also be plain text (`Title: <summary>`) — this conflict is resolved by **starting the report with the heading**, as it better serves both clarity and developer usability. The `Title:` rule is therefore **replaced** by the heading rule, and the `Title:` line is omitted.
- The `Error text:` line must contain **only** backticks for the error message, and no other formatting. This is satisfied by placing the error message in a line starting with `Error text: ` and using backticks only there.
- The `Reproducibility`, `Environment`, and `Severity` fields must all be included in the report, even if they conflict in format with other rules.

## Final Output Structure

The final bug report must include, in this exact order:

1. `## Bug: <summary>`
2. `Reported by: <full name>`
3. `Regression: yes`, `no`, or `unknown`
4. `Reproducibility: always`, `sometimes`, or `once`
5. `Expected: <what should happen>`
6. `Actual: <what actually happens>`
7. `Workaround: <description> or none`
8. `Error text: <exact error message in backticks>`
9. `Environment: <app version> <browser> on <platform>`

All lines must be plain text. Code formatting is forbidden except in the `Error text:` line, where backticks are used only to quote the error message.

## Example

## Bug: Graph fails to render after selecting date range in analytics tab

Reported by: Thomas Young  
Regression: unknown  
Reproducibility: always  
Expected: The graph should display data based on the selected date range.  
Actual: The graph displays a blank canvas and does not render any data.  
Workaround: none  
Error text: TypeError: Cannot read property 'length' of null  
Environment: App version 5.0.3, Chrome 123 on Windows 11  
Severity: S3

</skill>
