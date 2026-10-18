---
name: review-combined
description: Write code review comments using either the triage format or the mentoring style based on the context. Use for any code review comment.
---

# review-combined

A combined review comment can use either the triage format or the mentoring style, depending on the context. The triage format is used when brevity and clarity are crucial, while the mentoring style is used when teaching and dialogue are important.

## Rules

- **Triage Format**:
  - The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
  - Propose the change on a line that starts with `Proposed fix: `.
  - Give the place in the code on its own line as `Location: <file>:<line>`.
  - Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
  - State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
  - Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

- **Mentoring Style**:
  - Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.
  - Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
  - The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
  - Name one good thing about the diff on a line that starts with `What works well: `.
  - Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
  - Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

Where both formats apply, the rule from `review-triage` takes precedence.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output (using Triage Format):

```
[major] Retry loop also retries authentication errors

Location: src/uploader.py:88
The loop catches every exception, so a bad credential is retried five times before it fails.
Proposed fix: catch only timeout and throttling errors and re-raise everything else.
Confidence: high
Verdict: request changes
```

Output (using Mentoring Style):

```
Review: Retry loop also retries authentication errors

What works well: the backoff between attempts is clear and easy to follow.
Category: correctness
Effort: S
The loop in src/uploader.py catches every exception, so a bad credential is retried five times. Was that intended, or should only timeouts be retried?
Verdict: request changes
```
