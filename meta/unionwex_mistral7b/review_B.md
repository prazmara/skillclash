---
name: review-mentoring+review-triage
description: Combined rules of `review-mentoring` and `review-triage`. Use for any code review comment.
---

# Combined skill: review-mentoring + review-triage

Follow every rule below.

## Rules from `review-mentoring`

- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Name one good thing about the diff on a line that starts with `What works well: `.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## Rules from `review-triage`

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Propose the change on a line that starts with `Proposed fix: `.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

If two rules cannot both hold, the rule from `review-mentoring` wins.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
Review: Retry loop for S3 upload

What works well: The retry loop is implemented to handle exceptions during S3 upload.
Proposed fix: Consider adding a condition to exclude authentication errors from the retry loop.

Confidence: medium
Effort: M
- Findings:
  - Issue 1: The retry loop is currently retrying on authentication errors, which may lead to infinite retries if the authentication credentials are incorrect.
  - Issue 2: It might be more appropriate to handle authentication errors separately, such as by prompting the user to re-enter their credentials or by raising an exception that can be handled at a higher level.

Open question: Is there any specific reason for retrying on authentication errors in this case?
```
