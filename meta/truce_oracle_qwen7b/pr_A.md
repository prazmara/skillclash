---
name: pr-structured+pr-release-ready
description: Merged skill that replaces `pr-structured` and `pr-release-ready`. Use for any pull request description.
---

# Merged skill: pr-structured + pr-release-ready

This skill replaces `pr-structured` and `pr-release-ready`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-structured`

- The first line must be a level-1 Markdown heading with the title, starting with `# `.
- Include a section with the exact heading `## Summary`.
- Include a section with the exact heading `## Testing`.
- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Give the tracker ticket on its own line as `Ticket: <ID>`.

## Rules kept unchanged from `pr-release-ready`

- Include a section with the exact heading `## Rollback`.
- Name the reviewers on a line `Reviewers: @handle`.
- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Keep the whole description to at most 120 words and include a `## Risks` section with at least two bullet points starting with `- `.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add rate limiting to the login endpoint

## Summary
This PR adds rate limiting to the login endpoint to prevent brute force attacks.

## Testing
- [ ] Manually tested rate limiting functionality
- [ ] Added unit tests for rate limiting

## Rollback
If rate limiting causes issues, revert the changes and re-enable after investigating.

## Risks
- Misconfiguration could lead to unexpected rate limits affecting legitimate users.
- Potential performance impact on high traffic scenarios.

Ticket: AUTH-207  
Reviewers: @sam  
Labels: security, backend
```
