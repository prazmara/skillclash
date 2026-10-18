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

- Include a `## Risks` section with at least two bullet points starting with `- `, and keep the whole description to at most 120 words.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: Add rate limiting to the login endpoint

## Summary
This PR introduces rate limiting to the login endpoint to prevent brute force attacks.

## Risks
- Introducing rate limiting may affect legitimate users who frequently attempt to log in.
- Misconfiguration could lead to unexpected behavior.

## Testing
- [ ] Manually tested rate limiting with multiple failed login attempts.
- [ ] Verified that successful logins are not affected by rate limiting.

## Rollback
If issues arise, revert the commit and remove the rate limiting configuration. Update the environment variables to their previous values.

Reviewers: @sam
Labels: security, backend
Ticket: AUTH-207
```
