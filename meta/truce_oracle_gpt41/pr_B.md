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

- Keep the whole description to at most 120 words and include a `## Risks` section with at least two bullet points that start with `- `.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: add rate limiting to the login endpoint

## Summary
This PR introduces rate limiting to the login endpoint to mitigate brute-force attacks. The implementation restricts the number of login attempts per IP within a defined time window, enhancing security and protecting user accounts.

## Testing
- [x] Verified rate limiting blocks excessive login attempts.
- [x] Confirmed normal login flow is unaffected for legitimate users.

## Risks
- Rate limiting may inadvertently block legitimate users with shared IPs.
- Misconfiguration could lead to denial of service for all users.

## Rollback
Revert the changes to the login endpoint and remove the rate limiting middleware.

Reviewers: @sam  
Labels: security, backend  
Ticket: AUTH-207
```
