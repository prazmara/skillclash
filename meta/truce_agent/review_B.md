---
name: review-mentoring+review-triage
description: Merged skill that replaces `review-mentoring` and `review-triage`. Use for any code review comment.
---

# Merged skill: review-mentoring + review-triage

This skill replaces `review-mentoring` and `review-triage`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-mentoring`

- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## Rules kept unchanged from `review-triage`

- Propose the change on a line that starts with `Proposed fix: `.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark, only on a final line that starts with `Open question:` and comes after the `Verdict:` line. State every finding as a statement, so no question mark may appear anywhere above that final line.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
Review: Retry loop also retries authentication errors

Location: src/uploader.py:88
What works well: the retry loop makes the S3 upload robust against transient failures.
Category: correctness
The loop retries on every exception, so an authentication error is retried instead of failing at once.
Proposed fix: retry only on timeout and throttling errors and re-raise everything else.
Effort: S
Confidence: high
Verdict: request changes
Open question: Was retrying on authentication errors intended?
```
