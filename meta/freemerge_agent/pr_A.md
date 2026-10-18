---
name: pr-structured-release-ready
description: Write pull request descriptions with the team's fixed, short section layout that release managers can also act on. Use for any pull request.
---

# pr-structured-release-ready

This skill merges `pr-structured` and `pr-release-ready` and replaces both. Reviewers skim many pull requests, so a fixed, short layout lets them find what they need. Release managers decide from the description alone whether a change can ship, so it also covers risk and rollback.

Every rule of both skills is kept. Where two rules cannot both hold, `pr-structured` wins.

## Rules

- The first line must be a level-1 Markdown heading with the title, starting with `# `. This is the `pr-structured` rule. It overrides the `pr-release-ready` rule that the first line is plain text of the form `PR: <title>` with no Markdown heading, so no `PR:` line is written.
- Give the tracker ticket on its own line as `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Include a section with the exact heading `## Summary`.
- Include a `## Risks` section with at least two bullet points that start with `- `.
- Include a section with the exact heading `## Testing`.
- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Include a section with the exact heading `## Rollback`.
- Keep the whole description to at most 120 words. All the lines and sections above have to fit inside this limit, so write one short sentence under Summary and under Rollback and keep every bullet to a few words. Count the words before answering and never drop a required line or section to save space.

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

## Risks
- Users behind a shared IP address may hit the limit.
- The limiter offers no protection if its counter store is down.

## Testing
- [x] Unit tests for the limiter
- [ ] Load test on staging

## Rollback
Revert this pull request; no migration is involved.
```
