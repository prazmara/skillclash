---
name: pr-release-ready-structured
description: Write pull request descriptions that are actionable for release managers and follow the team's fixed section layout. Use for any pull request.
---

# pr-release-ready-structured

Release managers and reviewers need clear, actionable pull request descriptions. This skill combines risk and rollback coverage with a fixed, skimmable section layout.

## Rules

- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- Include a section with the exact heading `## Summary`.
- Include a section with the exact heading `## Risks` with at least two bullet points that start with `- `.
- Include a section with the exact heading `## Rollback`.
- Include a section with the exact heading `## Testing`.
- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Keep the whole description to at most 120 words.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: Add rate limiting to the login endpoint

Ticket: AUTH-207
Reviewers: @sam
Labels: security, backend

## Summary
Adds a sliding-window rate limiter to the login endpoint, allowing five attempts per minute per IP. Excess attempts receive a 429 response and are logged for security review.

## Risks
- Users sharing an IP may hit the limit and be blocked.
- If Redis is unavailable, the limiter fails open and offers no protection.

## Rollback
Revert this pull request and flush limiter keys from Redis. No schema or config changes, so rollback is safe at any time.

## Testing
- [x] Unit tests for rate limiting logic
- [ ] Load test on staging with multiple IPs
```
