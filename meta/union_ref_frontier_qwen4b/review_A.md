<skill>
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

## Resolution of Conflicts

If two rules conflict, the rule from `review-triage` takes precedence. Specifically:

- The first line must start with a severity tag (e.g., `[blocker]`) and include a short title — this overrides the requirement that the first line be plain text `Review: <title>`.
- The rule `Propose the change on a line that starts with `Proposed fix: `` must be satisfied, even if it conflicts with the `Review: <title>` format.

Therefore, the correct format for the first line is:  
`[severity] <title>`  
This satisfies both the severity tagging requirement from `review-triage` and ensures the first line is a statement (not a standalone review title).

## Example Output

[blocker] Debug mode enabled by default in production  
Proposed fix: Set DEBUG_MODE to False in production environments by default.  
Location: config/debug.py:15  
Category: security  
Confidence: high  
Effort: M  
What works well: The configuration is clearly named and easy to locate.  
Verdict: request changes  
Open question: Should we require explicit configuration to enable debug mode in production environments?
</skill>
