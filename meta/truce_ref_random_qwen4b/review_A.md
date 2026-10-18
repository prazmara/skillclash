<skill>
---
name: review-triage+review-mentoring
description: Merged skill that replaces `review-triage` and `review-mentoring`. Use for any code review comment. Follow every rule below.
---

# Merged skill: review-triage + review-mentoring

This skill replaces `review-triage` and `review-mentoring`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-triage`

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Rules kept unchanged from `review-mentoring`

- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Proposed fix: [insert proposed fix here]  
  Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.  
  This question must appear on a line starting with `Open question:` to satisfy both the statement rule and the question rule.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
[minor] Retries on all exceptions including authentication errors  
Location: src/uploader.py:88  
Verdict: request changes  
Category: correctness  
What works well: The retry loop adds resilience to transient failures.  
Effort: M  
Proposed fix: Change the retry logic to only retry on specific exceptions like NetworkError or ServiceError, and not on authentication errors.  
Open question: How should we handle authentication failures in the upload process?  
Confidence: high
```
</skill>
