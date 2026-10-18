---
name: review-mentoring+review-triage
description: Merged skill that replaces `review-mentoring` and `review-triage`. Use for any code review comment.
---

# Merged skill: review-mentoring + review-triage

This skill replaces `review-mentoring` and `review-triage`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-mentoring`

- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.

## Rules kept unchanged from `review-triage`

- Give the place in the code on its own line as `Location: <file>:<line>`.
- Propose the change on a line that starts with `Proposed fix: `.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`. Open question: Did you intend for all clarifying questions to be formatted as statements with a final question marked explicitly?
