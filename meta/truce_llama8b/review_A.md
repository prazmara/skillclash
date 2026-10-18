---
name: review-triage+review-mentoring
description: Merged skill that replaces `review-triage` and `review-mentoring`. Use for any code review comment.
---

# Merged skill: review-triage + review-mentoring

This skill replaces `review-triage` and `review-mentoring`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-triage`

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.

## Rules kept unchanged from `review-mentoring`


## Reconciled rules (each one satisfies a rule of both skills at once)

- Propose the change on a line that starts with `Proposed fix: `, and immediately below it, name one good thing about the diff on a line that starts with `What works well: `.
- To satisfy both rules, write the code location on its own line as "Location: <file>:<line>" followed by a clarifying question for the author, such as "Can you explain the reasoning behind this code?"
- State every finding as a statement, and classify each comment with a category label (`Category: correctness`, `Category: security`, `Category: performance`, `Category: readability`, or `Category: testing`) followed by a colon and a space, then the comment itself. If a comment is a question, it should start with `Open question:`.
- To satisfy both rules, write each line with a confidence level and an effort estimate, in the format: "Confidence: [high/medium/low] | Effort: [S/M/L]".

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
