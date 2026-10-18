---
name: review-mentoring-triage
description: Write code review comments that combine the mentoring style of the guild with the triage format of the merge queue. Use for any code review comment.
---

# review-mentoring-triage

A review comment should teach as well as correct, so it names what is good, classifies the problem, and opens a dialogue with the author. It also uses a fixed triage format so authors can quickly see the seriousness and location of the comment.

## Rules

- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Propose the change on a line that starts with `Proposed fix: `.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.
- State every finding as a statement. Ask the author at least one clarifying question, written as a full sentence that ends with a question mark. The question may only appear on a final line that starts with `Open question:`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
Review: Retry loop also retries authentication errors

What works well: the backoff between attempts is clear and easy to follow.
Category: correctness
Location: src/uploader.py:88
The loop catches every exception, so a bad credential is retried five times before it fails.
Proposed fix: catch only timeout and throttling errors and re-raise everything else.
Effort: S
Confidence: high
Open question: Was it intended to retry on authentication errors, or should only timeouts be retried?
Verdict: request changes
```
