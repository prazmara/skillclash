---
name: review-merged
description: Write code review comments using a merged format that combines mentoring depth with triage clarity. Use for any code review comment.
---

# review-merged

A review comment should teach as well as correct, while enabling fast triage. It combines mentoring-style reflection with structured triage metadata.

## Rules

- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Include a severity tag on the same line as the title, formatted as one of `[blocker]`, `[major]`, `[minor]`, `[nit]`.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- State the problem clearly as a statement.
- Propose the change on a line that starts with `Proposed fix: `.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.
- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark. This must appear on a line starting with `Open question:`.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
Review: [major] Retry loop also retries authentication errors

What works well: the backoff between attempts is clear and easy to follow.
Location: src/uploader.py:88
The loop catches every exception, so a bad credential is retried five times before it fails.
Category: correctness
Proposed fix: catch only timeout and throttling errors and re-raise everything else.
Effort: S
Confidence: high
Open question: Was that intended, or should only transient errors be retried?
Verdict: request changes
```
