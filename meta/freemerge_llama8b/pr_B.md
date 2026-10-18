<skill>
---
name: pr-release-ready
description: Write pull request descriptions that release managers can act on. Use for any pull request.
---

# pr-release-ready

Release managers decide from the description alone whether a change can ship, so it must cover risk and rollback.

## Rules

- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- Include a section with the exact heading `## Rollback`.
- Include a `## Risks` section with at least two bullet points that start with `- `.
- Under `## Risks`, list at least two checklist items written as `- [ ]` or `- [x]`.
- Include a section with the exact heading `## Testing`.
- Give the tracker ticket on its own line as `Ticket: <ID>`.
- Include a section with the exact heading `## Summary`.
- Keep the whole description to at most 120 words.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: Add rate limiting to the login endpoint

Ticket: AUTH-207
Reviewers: @sam
Labels: security, backend

## Risks
- [ ] Users behind a shared office IP address may reach the limit during busy periods and see errors.
- [ ] If the Redis cluster that stores the counters is unavailable, the limiter fails open and offers no protection.
- [ ] The new audit log entries increase log volume during an attack.

## Testing
- [x] Unit tests for the limiter
- [ ] Load test on staging

## Rollback
Revert this pull request and flush the limiter keys from Redis. No schema or configuration migration is involved, so the rollback is safe at any time.

## Summary
Limits login attempts to five per minute per IP address.
```
</skill>
