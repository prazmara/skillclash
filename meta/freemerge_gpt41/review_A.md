---
name: review-triage-mentoring
description: Write code review comments that combine the triage format of the merge queue with the mentoring style of the guild. Use for any code review comment.
---

# review-triage-mentoring

This skill combines the structured triage format with the mentoring approach. Comments clearly indicate severity, location, and outcome, while also teaching, classifying, and opening a dialogue with the author.

## Rules

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Propose the change on a line that starts with `Proposed fix: `.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.
- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark, on a line that starts with `Open question:`.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
[major] Retry loop also retries authentication errors

Location: src/uploader.py:88
The loop catches every exception, so a bad credential is retried five times before it fails.
What works well: the backoff between attempts is clear and easy to follow.
Category: correctness
Proposed fix: catch only timeout and throttling errors and re-raise everything else.
Confidence: high
Effort: S
Open question: Was it intended to retry on all exceptions, or should only timeouts be retried?
Verdict: request changes
```
