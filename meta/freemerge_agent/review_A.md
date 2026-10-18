---
name: review-triage-mentoring
description: Write code review comments in the triage format used by the merge queue, with the mentoring elements of the guild. Use for any code review comment.
---

# review-triage-mentoring

This skill merges `review-triage` and `review-mentoring` and replaces both. Authors receive many review comments, so a fixed triage format tells them at a glance how serious a comment is and where it applies. A review comment should also teach as well as correct, so it names what is good, classifies the problem and opens a dialogue with the author.

Every rule of both skills is kept. Where two rules cannot both hold, `review-triage` wins.

## Rules

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title. This is the `review-triage` rule. It overrides the `review-mentoring` rule that the first line is plain text of the form `Review: <title>` with no tag or bracket before it, so no `Review:` line is written.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.
- Name one good thing about the diff on a line that starts with `What works well: `.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Propose the change on a line that starts with `Proposed fix: `.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark. To keep the question mark rule above, the question goes on the final line of the comment, after the verdict, written as `Open question: <question>`. No other line contains a question mark.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
[major] Retry loop also retries authentication errors

Location: src/uploader.py:88
Category: correctness
Effort: S
What works well: the backoff between attempts is clear and easy to follow.
The loop catches every exception, so a bad credential is retried five times before it fails.
Proposed fix: catch only timeout and throttling errors and re-raise everything else.
Confidence: high
Verdict: request changes
Open question: Was retrying on authentication errors intended, or should only timeouts be retried?
```
