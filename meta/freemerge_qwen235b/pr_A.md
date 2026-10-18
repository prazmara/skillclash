---
name: pr-structured
description: Write pull request descriptions with the team's fixed section layout. Use for any pull request.
---

# pr-structured

Reviewers skim many pull requests. A fixed, short layout lets them find what they need. Release managers must also be able to act on the description, so risk and rollback information are included.

## Rules

- The first line must be a level-1 Markdown heading with the title, starting with `# `.
- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Include a section with the exact heading `## Summary`.
- Include a section with the exact heading `## Testing`.
- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Include a `## Risks` section with at least two bullet points that start with `- `.
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
- Users behind a shared office IP may hit the limit during busy periods.
- If Redis is down, the limiter fails open and offers no protection.

## Rollback
Revert the PR and flush limiter keys from Redis. No migrations, safe to rollback.
```
