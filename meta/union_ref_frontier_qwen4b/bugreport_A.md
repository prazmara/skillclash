<skill>
---
name: bug-triage-form+bug-dev-handoff
description: Combined rules of `bug-triage-form` and `bug-dev-handoff`. Use for any bug report.
---

# Combined skill: bug-triage-form + bug-dev-handoff

Follow every rule below.

## Rules from `bug-triage-form`

- Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- The first line must be plain text of the form `Title: <one-line summary>`.
- Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.
- Give the app version and the platform on one line that starts with `Environment: `.
- Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.

## Rules from `bug-dev-handoff`

- The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`.
- Name the person who found the bug on a line `Reported by: <full name>`.
- Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.
- Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- Quote the exact error message inside backticks so that developers can search for it.

## Conflict Resolution

If two rules cannot both hold, the rule from `bug-triage-form` wins.  
However, to satisfy both the `bug-triage-form` and `bug-dev-handoff` requirements simultaneously, the following compromise is implemented:

- The **first line** must be a **plain text line** of the form `Title: <one-line summary>`, **not** a Markdown heading. This satisfies `bug-triage-form` and **overrides** the `bug-dev-handoff` rule that requires a Markdown heading.  
  > *Note: This is a necessary conflict resolution to preserve all `bug-triage-form` rules, even if it appears to contradict `bug-dev-handoff`. The `bug-triage-form` rule takes precedence when in conflict.*

- The **`Expected:`** and **`Actual:`** lines must appear exactly once each, in that order, as required by both skills. This ensures consistency.

- The **`Environment:`** line must be present and formatted as `Environment: <app version> on <platform>`, as required by `bug-triage-form`.

- The **`Reproducibility:`** line must be included with one of: `Reproducibility: always`, `Reproducibility: sometimes`, or `Reproducibility: once`.

- The **`Severity:`** line must be included with one of: `Severity: S1`, `Severity: S2`, `Severity: S3`, or `Severity: S4`.

- The **`Reported by:`** line must be included with the full name of the reporter, as required by `bug-dev-handoff`.

- The **`Regression:`** line must be included with one of: `Regression: yes`, `Regression: no`, or `Regression: unknown`.

- The **`Workaround:`** line must be included, with `Workaround: none` if no workaround exists.

- The **error message** must be quoted in backticks and appear only on a final line starting with `Error text:`, as required by both skills. This satisfies the backtick rule from `bug-triage-form` and the quoting requirement from `bug-dev-handoff`.

## Example Output

Title: Profile edit form crashes when saving a profile with avatar from public URL  
Reported by: James Reed  
Reproducibility: always  
Expected: The user profile is saved successfully with the avatar from the public URL.  
Actual: The profile edit form crashes with an error when attempting to save.  
Environment: 5.1.0 on Firefox 118 Windows 10  
Severity: S3  
Regression: unknown  
Workaround: none  
Error text: Cannot assign to read only property 'value' of object

Title: Calendar view shifts incorrectly when switching between months in a multi-year range  
Reported by: Kevin Chang  
Reproducibility: always  
Expected: The calendar view should display the correct month and year when switching between months in a multi-year range.  
Actual: The calendar view shifts incorrectly, showing the wrong month or year, especially when moving between years.  
Environment: 3.9.1 on Chrome 121 Windows 10  
Severity: S2  
Regression: unknown  
Workaround: none  
Error text: RangeError: Invalid date

Title: Export PDF function generates corrupted file with missing fonts when formatting report with large text blocks  
Reported by: Robert Garcia  
Reproducibility: always  
Expected: The exported PDF should contain all text blocks with proper font rendering, including bold text.  
Actual: The exported PDF is corrupted and missing fonts, especially in large text blocks where bold text appears as blank or garbled.  
Environment: 4.0.8 on Edge 118 Windows 11  
Severity: S3  
Regression: unknown  
Workaround: none  
Error text: Font not found: Arial-Bold
</skill>
