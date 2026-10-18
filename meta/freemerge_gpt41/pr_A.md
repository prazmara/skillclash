---
name: pr-structured-release
description: Write pull request descriptions that follow the team's fixed section layout and provide all information needed for release managers. Use for any pull request.
---

# pr-structured-release

Reviewers and release managers need to quickly find key information in pull request descriptions. Use a fixed, concise layout that covers summary, testing, risk, rollback, ticket, reviewers, and labels.

## Rules

- The first line must be a level-1 Markdown heading with the title, starting with `# `.
- Give the tracker ticket on its own line as `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Include a section with the exact heading `## Summary`.
- Include a section with the exact heading `## Testing`.
    - Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Include a section with the exact heading `## Risks`.
    - Under Risks, include at least two bullet points that start with `- `.
- Include a section with the exact heading `## Rollback`.
- Keep the whole description to at most 120 words.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add rate limiting to the login endpoint

Ticket: AUTH-207
Reviewers: @sam
Labels: security, backend

## Summary
Limits login attempts to five per minute per IP address.

## Testing
- [x] Unit tests for the limiter
- [ ] Load test on staging

## Risks
- Users behind a shared IP may hit the limit and see errors.
- If Redis is down, rate limiting is bypassed.

## Rollback
Revert this pull request and flush limiter keys from Redis.
```
