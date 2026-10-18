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
