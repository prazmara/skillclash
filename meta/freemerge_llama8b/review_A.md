<skill>
---
name: review-triage-mentoring
description: Write code review comments in the triage format used by the merge queue, while teaching and mentoring the author. Use for any code review comment.
---

# review-triage-mentoring

A review comment should tell the author what is good, classify the problem, and open a dialogue, all while using the triage format to tell the author at a glance how serious a comment is and where it applies.

## Rules

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark, on a line that starts with `Was that intended: ` or `Open question:`.
- Propose the change on a line that starts with `Proposed fix: `.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- State every finding as a statement. A question mark may appear only on a line that starts with `Was that intended: ` or `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
[major] Retry loop also retries authentication errors

What works well: the backoff between attempts is clear and easy to follow.
Location: src/uploader.py:88
The loop catches every exception, so a bad credential is retried five times. Was that intended, or should only timeouts be retried?
Category: correctness
Proposed fix: catch only timeout and throttling errors and re-raise everything else.
Confidence: high
Effort: S
Verdict: request changes
```
</skill>
