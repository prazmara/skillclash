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

- Write a description of no more than 120 words, including a "## Risks" section with at least two bullet points starting with `- `, to ensure compliance with both the `pr-structured` and `pr-release-ready` rules.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add rate limiting to the login endpoint

## Summary

This pull request adds rate limiting to the login endpoint to prevent brute force attacks and improve the security of our application.

## Testing
- [ ] Unit tests have been run and passed
- [ ] End-to-end tests have been run and passed

## Risks
- The rate limiting implementation may affect legitimate users if not properly configured.
- There may be performance impacts due to the additional checks required for rate limiting.

## Rollback
In case of any issues, the rate limiting can be temporarily disabled by modifying the configuration settings.

## Ticket
AUTH-207

## Reviewers
@sam

## Labels
security, backend
