---
name: review-mentoring+review-triage
description: Merged skill that replaces `review-mentoring` and `review-triage`. Use for any code review comment.
---

# Merged skill: review-mentoring + review-triage

This skill replaces `review-mentoring` and `review-triage`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-mentoring`

- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

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

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
Review: S3 Upload Retry Logic

Category: correctness
What works well: The retry loop ensures robustness against transient errors during S3 uploads.
Proposed fix: Consider limiting the number of retries and implementing exponential backoff to avoid potential resource exhaustion.
Location: src/uploader.py:88
Verdict: request changes
Effort: M
Confidence: high
Open question: How will the retry mechanism behave in case of persistent authentication errors?
Confidence: high
Confidence: medium
Confidence: low
Verdict: comment
```
