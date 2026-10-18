---
name: review-mentoring+review-triage
description: Merged skill that replaces `review-mentoring` and `review-triage`. Use for any code review comment.
---

# Merged skill: review-mentoring + review-triage

This skill replaces `review-mentoring` and `review-triage`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-mentoring`

- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.

## Rules kept unchanged from `review-triage`

- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write an output that follows this format: ``` What works well: [One good thing about the diff] Proposed fix: [Change to be made] ``` In the same line, provide one good thing about the diff and propose the change to be made.
- Write responses in the following format: "Estimate the work needed on a line (Effort: S, M, or L), and state every finding as a statement. A question mark may appear only on a final line that starts with 'Open question:'. For example: Effort: M - Findings: - Issue 1: Description of issue 1 - Issue 2: Description of issue 2 - Open question: Is there any additional information needed to address these issues?"

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
