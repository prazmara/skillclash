---
name: review-triage-mentoring
description: Write code review comments in the mentoring style of the guild, with the triage fields used by the merge queue. Use for any code review comment.
---

# review-triage-mentoring

This skill merges `review-triage` and `review-mentoring` and replaces both. A review comment should teach as well as correct, so it names what is good, classifies the problem and opens a dialogue with the author. Authors also receive many review comments, so fixed triage fields tell them at a glance how serious a comment is and where it applies.

Every rule of both skills is kept. Where two rules cannot both hold, `review-mentoring` wins.

## Rules

- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it. This is the `review-mentoring` rule. It overrides the `review-triage` rule that the first line starts with a severity tag in square brackets. So that the severity is not lost, give the tag on its own line below the first line as `Severity: [blocker]`, `Severity: [major]`, `Severity: [minor]` or `Severity: [nit]`. The first line itself contains no square brackets.
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
Review: Retry loop also retries authentication errors

Severity: [major]
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
