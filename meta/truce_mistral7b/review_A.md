---
name: review-triage+review-mentoring
description: Merged skill that replaces `review-triage` and `review-mentoring`. Use for any code review comment.
---

# Merged skill: review-triage + review-mentoring

This skill replaces `review-triage` and `review-mentoring`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-triage`

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Rules kept unchanged from `review-mentoring`

- Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.
- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: ``` Proposed fix: [Your proposed change here] What works well: [Something positive about the current code or diff] ``` Ensure that the proposed fix and the positive comment are separated by a line break for clarity.
- Write responses that follow this format: 1. Each finding should be stated as a declarative sentence. (Use a period at the end.) 2. If applicable, include an estimate of the effort required (S, M, or L) at the end of the finding statement, preceded by "Effort:". 3. If there is an open question, start the line with "Open question:" and end it with a question mark. Example: "The code is not properly formatted according to the company's style guide. (Effort: M) Open question: Is it necessary to consult with the team lead about the formatting changes?"

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

[minor]
Location: src/uploader.py:88
Verdict: comment
Confidence: high

```
Proposed fix: None at this time, but consider the implications of retrying on authentication errors.
What works well: The retry loop handles exceptions well, improving the robustness of the S3 upload.

The retry loop retries on every exception, including authentication errors. (Effort: M)
Open question: Is it appropriate to retry on authentication errors?
```
