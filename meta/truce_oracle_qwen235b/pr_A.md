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

- Keep the whole description to at most 120 words and include a `## Risks` section with at least two bullet points that start with `- `. Both the word limit and the `## Risks` section with the required format must be satisfied in the same output.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add Rate Limiting to Login Endpoint

## Summary
Implemented rate limiting on the login endpoint to prevent brute-force attacks and abuse. The limit is set to 5 attempts per 15 minutes per IP address.

## Testing
- [ ] Verified rate limit blocks further attempts after 5 failed logins
- [ ] Confirmed successful login resets the counter

## Risks
- Legitimate users on shared IPs may be rate-limited
- Incorrect configuration could block valid traffic

## Rollback
Revert the middleware addition and configuration in the auth route if issues arise.

Ticket: AUTH-207
Reviewers: @sam
Labels: security, backend
```
