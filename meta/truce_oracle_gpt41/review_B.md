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

- State every finding as a statement, and only include a question mark on a final line that starts with `Open question:`. Use this final line to ask the author at least one clarifying question, written as a full sentence.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
Review: Retry loop wraps all exceptions, including authentication errors
What works well: Adding a retry loop increases robustness against transient errors during S3 uploads.
Category: correctness
Effort: M
Location: src/uploader.py:88
Proposed fix: Restrict the retry logic to only handle transient or recoverable exceptions (such as network errors or throttling), and allow authentication or permission errors to fail immediately without retrying.
Confidence: high
Verdict: request changes
Open question: Can you clarify which specific exceptions you intend to retry, and whether authentication errors should be excluded from the retry logic?
```
