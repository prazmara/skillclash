---
name: review-triage
description: Write code review comments in the triage format used by the merge queue. Use for any code review comment.
---

# review-triage

Authors receive many review comments. A fixed triage format tells them at a glance how serious a comment is and where it applies.

## Rules

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Propose the change on a line that starts with `Proposed fix: `.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
[major] Retry loop also retries authentication errors

Location: src/uploader.py:88
The loop catches every exception, so a bad credential is retried five times before it fails.
Proposed fix: catch only timeout and throttling errors and re-raise everything else.
Confidence: high
Verdict: request changes
```
