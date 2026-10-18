---
name: review-triage-mentoring
description: Write code review comments using a merged format that satisfies both triage severity tagging and mentoring guidance. Use for any code review comment.
---

# review-triage-mentoring

This skill combines the structured severity tagging of `review-triage` with the teaching and dialogue-oriented style of `review-mentoring`. The result is a review comment that clearly communicates urgency, provides educational value, and guides action.

## Rules

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Propose the change on a line that starts with `Proposed fix: `.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.
- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark, but only as part of an `Open question:` line.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
[major] Retry loop also retries authentication errors

Location: src/uploader.py:88
What works well: the backoff between attempts is clear and easy to follow.
Category: correctness
Effort: S
The loop catches every exception, so a bad credential is retried five times before it fails.
Proposed fix: catch only timeout and throttling errors and re-raise everything else.
Confidence: high
Open question: Was it intended to retry authentication failures, or should those fail fast?
Verdict: request changes
```
