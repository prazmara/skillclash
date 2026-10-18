<skill>
---
name: review-triage-mentoring
description: Write code review comments in the triage format used by the merge queue, while also mentoring the author. Use for any code review comment. If a rule from `review-triage` conflicts with a rule from `review-mentoring`, the rule from `review-triage` wins.
---

# review-triage-mentoring

Authors receive many review comments. A fixed triage format tells them at a glance how serious a comment is and where it applies. A mentoring style teaches as well as corrects, so it names what is good, classifies the problem and opens a dialogue with the author.

## Rules

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Propose the change on a line that starts with `Proposed fix: `.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.
- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

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

What works well: the backoff between attempts is clear and easy to follow.
Category: correctness
Effort: S
Was the intention to retry authentication errors? If not, consider removing the retry loop or modifying it to only retry timeout and throttling errors.
```
</skill>
