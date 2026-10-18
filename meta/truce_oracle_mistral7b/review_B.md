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

- Write responses that follow this format: 1. State every finding as a statement. (No question marks within statements.) 2. If a question is needed for clarification, end it with a question mark and place it after all statements and an `Open question:` line. Example: Findings: - The author has not provided a clear objective for the article. - The introduction does not engage the reader. - The conclusion lacks a call to action. Open question: - Could you please clarify the objective of this article?

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
Review: Retry loop for S3 upload

What works well: The addition of a retry loop for handling exceptions
Category: performance
Effort: M
Location: src/uploader.py:88

Findings:
- The retry loop retries on every exception, including authentication errors. This could potentially hide authentication issues and lead to unnecessary retries.

Proposed fix:
- Consider adding a condition to the retry loop that only retries on non-authentication errors.

Confidence: medium
```
