---
name: review-triage+review-mentoring
description: Merged skill that replaces `review-triage` and `review-mentoring`. Use for any code review comment.
---

# Merged skill: review-triage + review-mentoring

This skill replaces `review-triage` and `review-mentoring`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-triage`

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Propose the change on a line that starts with `Proposed fix: `.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.

## Rules kept unchanged from `review-mentoring`

- Name one good thing about the diff on a line that starts with `What works well: `.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write responses that consist of two parts: 1. Each finding should be stated as a complete sentence without a question mark. 2. End the response with an open question, starting with "Open question:", followed by a question mark. Example: Findings: The author has not provided a clear objective for the article. The introduction is too long and lacks a hook. Open question: Could you please clarify the main objective of your article and consider revising the introduction to make it more engaging?
