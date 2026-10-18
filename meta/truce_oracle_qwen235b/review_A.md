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

- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`. Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
[blocker] Retry loop catches all exceptions, including non-retryable ones like authentication errors  
Location: src/uploader.py:88  
Proposed fix: Narrow the exception types caught for retry to only transient errors (e.g., connection timeouts, throttling), and let authentication errors fail fast.  
Confidence: high  
Verdict: request changes  
What works well: The intent to improve reliability with retries is a good step toward resilience.  
Category: correctness  
Effort: M  
Open question: Did you consider which specific exception types are safe to retry, and how do you plan to distinguish transient from permanent failures?
```
