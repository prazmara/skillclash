---
name: pr-release-ready+pr-structured
description: Merged skill that replaces `pr-release-ready` and `pr-structured`. Use for any pull request description.
---

# Merged skill: pr-release-ready + pr-structured

This skill replaces `pr-release-ready` and `pr-structured`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-release-ready`

- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- Include a section with the exact heading `## Rollback`.
- Name the reviewers on a line `Reviewers: @handle`.
- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Put the ticket on a separate line in the form `Ticket: <ID>`.

## Rules kept unchanged from `pr-structured`

- Include a section with the exact heading `## Summary`.
- Include a section with the exact heading `## Testing`.
- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- "Include a `## Risks` section with at least two bullet points starting with `- `, and ensure the entire description does not exceed 120 words."

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: Add rate limiting to the login endpoint

Ticket: AUTH-207

Reviewer: @sam

Labels: security, backend

## Summary
This pull request introduces rate limiting to the login endpoint to enhance security by preventing brute force attacks.

## Testing
- [ ] Test rate limiting with various request intervals
- [ ] Verify that legitimate users are not affected by the new rate limiting

## Risks
- Potential false positives for legitimate users under high traffic
- Rate limiting thresholds may need adjustment based on user feedback

## Rollback
- Revert changes to the login endpoint rate limiting configuration
- Restore the previous behavior of the login endpoint
```
