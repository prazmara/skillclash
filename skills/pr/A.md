---
name: pr-structured
description: Write pull request descriptions with the team's fixed section layout. Use for any pull request.
---

# pr-structured

Reviewers skim many pull requests. A fixed, short layout lets them find what they need.

## Rules

- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Include a section with the exact heading `## Testing`.
- Give the tracker ticket on its own line as `Ticket: <ID>`.
- Include a section with the exact heading `## Summary`.
- The first line must be a level-1 Markdown heading with the title, starting with `# `.
- Keep the whole description to at most 120 words.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add rate limiting to the login endpoint

Ticket: AUTH-207

## Summary
Limits login attempts to five per minute per IP address.

## Testing
- [x] Unit tests for the limiter
- [ ] Load test on staging
```
