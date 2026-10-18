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

- ## Combined Rule Write a description that is 120 words or less, and include a `## Risks` section with at least two bullet points that start with `- ` within the first 120 words.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add rate limiting to the login endpoint

## Summary
This pull request adds rate limiting to the login endpoint to prevent brute-force attacks. The new rate limiting mechanism will block users who exceed the allowed number of login attempts within a certain time frame.

## Risks
- The rate limiting mechanism may block legitimate users who have forgotten their password and are trying to reset it.
- The rate limiting threshold may need to be adjusted based on user feedback and login attempt patterns.

## Testing
- [ ] Verify that the rate limiting mechanism is enabled and functioning correctly.
- [ ] Test the login endpoint with a high number of concurrent login attempts to ensure the rate limiting mechanism blocks the user.

## Rollback
If the rate limiting mechanism causes issues with legitimate users, we can rollback the changes by removing the rate limiting code and adjusting the login endpoint to use a different authentication mechanism.

## Reviewers: @sam
## Labels: security, backend
## Ticket: AUTH-207
```
