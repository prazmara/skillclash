---
name: pr-structured-release-ready
description: Write pull request descriptions that release managers can act on, in the team's fixed, short section layout. Use for any pull request.
---

# pr-structured-release-ready

This skill merges `pr-structured` and `pr-release-ready` and replaces both. Release managers decide from the description alone whether a change can ship, so it covers risk and rollback. Reviewers skim many pull requests, so the description also keeps a fixed, short layout that lets them find what they need.

Every rule of both skills is kept. Where two rules cannot both hold, `pr-release-ready` wins.

## Rules

- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title. This is the `pr-release-ready` rule. It overrides the `pr-structured` rule that the first line is a level-1 Markdown heading starting with `# `, so no `# ` heading is written anywhere. The section headings below stay level-2 headings.
- Put the tracker ticket on its own line in the form `Ticket: <ID>`.
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
PR: Add rate limiting to the login endpoint

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
