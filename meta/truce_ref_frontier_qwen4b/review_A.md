<skill>
---
name: review-triage+review-mentoring
description: Merged skill that replaces `review-triage` and `review-mentoring`. Use for any code review comment. Follow every rule below.
---

# Merged skill: review-triage + review-mentoring

This skill replaces `review-triage` and `review-mentoring`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `review-triage`

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Rules kept unchanged from `review-mentoring`

- Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- Name one good thing about the diff on a line that starts with `What works well:`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Proposed fix: [insert proposed fix here] Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.

## Important clarification:  
The rule "State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`" must be strictly followed.  
Therefore, any question mark in the output must appear **only** on a line that starts with `Open question:`.  
Any question mark in a proposed fix or other line is invalid and violates this rule.

Thus, in the `Proposed fix` line, the sentence must end with a question mark **only if** it is phrased as a full clarifying question and **only if** it starts with `Open question:`.  
However, the current `Proposed fix` format instructs to "ask the author at least one clarifying question" — this must be done **in a line that begins with `Open question:`**.

Therefore, we revise the reconciled rule to:

## Reconciled rules (each one satisfies a rule of both skills at once)

- Proposed fix: [insert proposed fix here]  
  Open question: [insert a full sentence ending with a question mark]

This ensures that the only line with a question mark starts with `Open question:` and satisfies both the need for a clarifying question and the strict rule on question placement.

## Example

Request: Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.

Output:

```
[minor] Retries on all exceptions including authentication errors  
Location: src/uploader.py:88  
Verdict: request changes  
Category: correctness  
What works well: The retry loop adds resilience to transient failures.  
Effort: M  
Confidence: medium  
Proposed fix: Change the retry logic to only retry on specific exceptions like NetworkError or ServiceError, and not on authentication errors.  
Open question: Should we handle authentication failures in the upload process by logging an error and failing gracefully instead?
```
</skill>
