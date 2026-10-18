---
name: review-triage+review-mentoring
description: Combined rules of `review-triage` and `review-mentoring`. Use for any code review comment.
---

# Combined skill: review-triage + review-mentoring

Follow every rule below.

## Rules from `review-triage`

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Propose the change on a line that starts with `Proposed fix: `.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Rules from `review-mentoring`

- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

If two rules cannot both hold, the rule from `review-triage` wins.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
[blocker] Unnecessary retry on authentication errors
Verdict: request changes
Location: src/uploader.py:88
Can you explain the reasoning behind this code?
Category: correctness: This retry loop will mask authentication errors, making it harder to diagnose and fix issues with AWS credentials.
Confidence: medium | Effort: M
Proposed fix: Remove the retry loop and let the application fail fast on authentication errors.
What works well: The diff is well-structured and easy to follow.
Open question: Are there any specific use cases where we want to retry on authentication errors?
```
