---
name: review-mentoring-triage
description: Write code review comments in the mentoring style of the guild, with a triage format for clarity. Use for any code review comment.
---

# review-mentoring-triage

A review comment should teach as well as correct, so it names what is good, classifies the problem and opens a dialogue with the author. Authors receive many review comments. A fixed triage format tells them at a glance how serious a comment is and where it applies.

## Rules

- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it, or start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`.
- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
[major] Retry loop also retries authentication errors

What works well: the backoff between attempts is clear and easy to follow.
Category: correctness
Location: src/uploader.py:88
The loop catches every exception, so a bad credential is retried five times before it fails.
Open question: Was that intended, or should only timeouts be retried?
Effort: S
Confidence: high
Verdict: request changes
```
