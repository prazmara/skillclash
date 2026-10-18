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

- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark. Open question: State every finding as a statement; a question mark may appear only on a final line that starts with `Open question:`.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
Review: Wrap S3 upload in retry loop

Location: src/uploader.py:88

Category: correctness
Effort: M
Confidence: medium

The retry loop catches all exceptions, which might hide issues like authentication problems. How do we handle different types of exceptions?

Proposed fix: Modify the retry loop to distinguish between transient and non-transient errors.

Open question: Should we log the error details when retrying?
```
