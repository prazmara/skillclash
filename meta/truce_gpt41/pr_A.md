---
name: pr-structured+pr-release-ready
description: Merged skill that replaces `pr-structured` and `pr-release-ready`. Use for any pull request description.
---

# Merged skill: pr-structured + pr-release-ready

This skill replaces `pr-structured` and `pr-release-ready`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-structured`

- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Include a section with the exact heading `## Testing`.
- Give the tracker ticket on its own line as `Ticket: <ID>`.
- Include a section with the exact heading `## Summary`.
- The first line must be a level-1 Markdown heading with the title, starting with `# `.

## Rules kept unchanged from `pr-release-ready`

- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Name the reviewers on a line `Reviewers: @handle`.
- Include a section with the exact heading `## Rollback`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Keep the whole description to at most 120 words and include a `## Risks` section with at least two bullet points that start with `- `. Both requirements must be satisfied in the same output.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add Rate Limiting to Login Endpoint

Ticket: AUTH-207  
Labels: security, backend  
Reviewers: @sam

## Summary

This PR introduces rate limiting to the login endpoint to mitigate brute-force attacks and enhance security. The implementation restricts the number of login attempts per IP within a defined time window.

## Testing

- [x] Verified rate limiting blocks excessive login attempts.
- [x] Confirmed normal login flow is unaffected for legitimate users.

## Risks

- May inadvertently block legitimate users with shared IPs.
- Misconfiguration could lead to denial of service for all users.

## Rollback

Revert this PR to remove rate limiting and restore previous login behavior.
```
