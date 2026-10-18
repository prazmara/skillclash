<skill>
---
name: review-mentoring+review-triage
description: Merged skill that replaces `review-mentoring` and `review-triage`. Use for any code review comment. Follow every rule below.
---

# Merged skill: review-mentoring + review-triage

This skill replaces `review-mentoring` and `review-triage`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-mentoring`

- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Name one good thing about the diff on a line that starts with `What works well:`.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## Rules kept unchanged from `review-triage`

- Give the place in the code on its own line as `Location: <file>:<line>`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark. This question must appear on a line starting with `Open question:`.
- Propose a concrete change to address the issue, written on a line that starts with `Proposed fix: `.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
Review: The retry loop retries on every exception, including authentication errors, which may lead to unnecessary retries and potential security issues.
Location: src/uploader.py:88
Category: correctness
Confidence: high
Effort: M
What works well: The retry mechanism ensures that transient errors are handled gracefully.
Open question: Should the retry loop exclude authentication errors to prevent failed uploads due to invalid credentials?
Proposed fix: Add a condition to skip retry on authentication errors.
Verdict: request changes
```
</skill>
