<skill>
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
- Name one good thing about the diff on a line that starts with `What works well:`.
- Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## Rules from `review-triage`

- The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- Propose the change on a line that starts with `Proposed fix:`.
- Give the place in the code on its own line as `Location: <file>:<line>`.
- Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

## Resolution of Conflicts

If two rules cannot both hold, the rule from `review-mentoring` wins.  
Specifically, **the first line must be plain text of the form `Review: <title>`** — this overrides any severity tag (e.g., `[blocker]`) in the first line.  
Therefore, the first line must be `Review: <title>`, and **no severity tag may appear at the beginning of the first line**.

The `Review: <title>` line must be followed by:
- `Location: <file>:<line>`
- `Category: <one of correctness, security, performance, readability, testing>`
- `What works well: <one positive observation>`
- `Proposed fix: <suggested change>`
- `Verdict: approve | request changes | comment`
- `Effort: S | M | L`
- `Confidence: high | medium | low`
- `Open question: <one full sentence ending in ?>` (only if applicable)

This ensures both the mentoring and triage rules are satisfied while resolving conflicts in favor of `review-mentoring` for the foundational structure of the review.

## Example Output (Correct and Complete)

Review: Debug mode enabled by default in production, exposing internal state  
Location: config/debug.py:15  
Category: security  
What works well: The diff clearly identifies the issue and specifies the file and line number.  
Proposed fix: Change the default value of DEBUG to False in production environments.  
Verdict: request changes  
Effort: M  
Confidence: high  
Open question: Should we add a configuration flag to allow admins to enable debug mode in production for troubleshooting?

</skill>
