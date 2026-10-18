---
name: review-mentoring+review-triage
description: Merged skill that replaces `review-mentoring` and `review-triage`. Use for any code review comment.
---

# Merged skill: review-mentoring + review-triage

This skill replaces `review-mentoring` and `review-triage`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-mentoring`

- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.

## Rules kept unchanged from `review-triage`


## Reconciled rules (each one satisfies a rule of both skills at once)

- Name one good thing about the diff on a line that starts with `What works well: ` and propose the change on a line that starts with `Proposed fix: `, by placing the proposed change immediately after the line that starts with `What works well: ` and starting the proposed change on a new line.
- Write the author's response to the clarifying question on the same line as the question, followed by `Location: <file>:<line>` on a new line.
- Classify the comment on a line as one of the following categories: `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability`, or `Category: testing`. State every finding as a statement, and if there are multiple findings, end with a line that starts with `Open question:`.
- Estimate the work needed on a line as `Effort: S` if the task is straightforward and requires minimal effort, `Effort: M` if the task is moderately complex and requires some effort, or `Effort: L` if the task is complex and requires significant effort. Express your confidence in the assessment as `Confidence: high` if you are very sure, `Confidence: medium` if you are somewhat sure, or `Confidence: low` if you are not very sure.
