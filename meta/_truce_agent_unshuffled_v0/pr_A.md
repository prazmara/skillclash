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

- Include a `## Risks` section with at least two bullet points that start with `- `, and keep each bullet to one short phrase of at most ten words. Keep the whole description to at most 120 words, counting every heading, label, checklist item and bullet, so keep every other section to one short sentence or its required list and add no extra paragraphs.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add rate limiting to the login endpoint

Ticket: AUTH-207
Reviewers: @sam
Labels: security, backend

## Summary
Adds rate limiting to the login endpoint.

## Testing
- [x] Unit tests for the limiter
- [ ] Load test on staging

## Risks
- Legitimate users on shared IP addresses may be blocked
- A wrong limit may lock out valid logins

## Rollback
Revert this pull request.
```
