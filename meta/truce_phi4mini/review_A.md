---
name: review-triage+review-mentoring
description: Merged skill that replaces `review-triage` and `review-mentoring`. Use for any code review comment.
---

# Merged skill: review-triage + review-mentoring

This skill replaces `review-triage` and `review-mentoring`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-triage`

- [blocker]
- Proposed fix:
- Location: <file>:<line>
- Verdict: approve
- Verdict: request changes
- Verdict: comment
- Open question:
- Confidence: high
- Confidence: medium
- Confidence: low

## Rules kept unchanged from `review-mentoring`

- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
Review: S3 upload retry logic

Proposed fix: Implement exponential backoff and circuit breaker pattern to handle retries more efficiently.

Location: src/uploader.py:88

Verdict: request changes

Effort: M

What works well: The retry mechanism ensures that transient errors do not cause immediate failure.

Verdict: request changes

Effort: M

Ask the author at least one clarifying question: Could you explain the rationale behind retrying on every exception, including authentication errors, and whether there are any specific scenarios where this approach is necessary?
```
