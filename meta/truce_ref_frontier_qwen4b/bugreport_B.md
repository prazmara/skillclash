<skill>
---
name: bug-dev-handoff+bug-triage-form
description: Merged skill that replaces `bug-dev-handoff` and `bug-triage-form`. Use for any bug report.
---

# Merged skill: bug-dev-handoff + bug-triage-form

This skill replaces `bug-dev-handoff` and `bug-triage-form`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `bug-dev-handoff`

- Name the person who found the bug on a line `Reported by: <full name>`.
- Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Quote the exact error message inside backticks so that developers can search for it.

## Rules kept unchanged from `bug-triage-form`

- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Start with plain text `Title: <one-line summary>`, then on the next line add a level-2 Markdown heading `## Bug: <summary>`, ensuring both the title and bug heading use the exact same summary content.
- If the issue works before and happens consistently, output `Regression: yes` and `Reproducibility: always`. Otherwise, output `Regression: no` or `Reproducibility: sometimes`, and `Regression: unknown` if neither can be determined.

## Corrected rule (added to fix broken formatting)

- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.  
  → **Clarification**: The error message must be quoted with backticks only on a line that starts with `Error text:`. However, the original skill already requires quoting the error message in backticks. To satisfy both, we now **require that the error message be presented exactly as a line starting with `Error text:`**, and that backticks are used only on that line. This replaces the previous rule that allowed backticks in the middle of the description.

## Final formatting rule (to fix the broken output)

- The first line of the output must be `Title: <one-line summary>`, followed immediately by a line with a level-2 Markdown heading `## Bug: <summary>`. No other content or formatting should appear before this.
- After the heading, the rest of the content must follow the exact structure: `Reported by: ...`, `Expected: ...`, `Actual: ...`, `Workaround: ...`, and the error message line starting with `Error text:` (in backticks), then `Environment: ...`, and finally `Severity: ...`, `Regression: ...`, `Reproducibility: ...`.

## Example

Request: Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.

Output:

```
Title: CSV export produces empty file when date filter spans more than 90 days
## Bug: CSV export produces empty file when date filter spans more than 90 days

Reported by: Ivo Marek  
Expected: The CSV export should contain data for the selected date range.  
Actual: The CSV export produces an empty file when the date filter spans more than 90 days.  
Workaround: none  
Error text: `TypeError: rows is undefined`  

Environment: App version 3.8.1, Chrome 122 on Windows 11  
Severity: S2  
Regression: yes  
Reproducibility: always
```
</skill>
