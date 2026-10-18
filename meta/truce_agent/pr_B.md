---
name: pr-release-ready+pr-structured
description: Merged skill that replaces `pr-release-ready` and `pr-structured`. Use for any pull request description.
---

# Merged skill: pr-release-ready + pr-structured

This skill replaces `pr-release-ready` and `pr-structured`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-release-ready`

- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- Include a section with the exact heading `## Rollback`.

## Rules kept unchanged from `pr-structured`

- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Include a section with the exact heading `## Testing`.
- Include a section with the exact heading `## Summary`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Include a `## Risks` section with at least two bullet points that start with `- `, and keep each bullet to one short phrase of at most ten words. Keep the whole description to at most 120 words, counting every heading, label, checklist item and bullet, so keep every other section to one short sentence or its required list and add no extra paragraphs.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: Add rate limiting to the login endpoint

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
