---
name: pr-release-ready+pr-structured
description: Merged skill that replaces `pr-release-ready` and `pr-structured`. Use for any pull request description.
---

# Merged skill: pr-release-ready + pr-structured

This skill replaces `pr-release-ready` and `pr-structured`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-release-ready`

- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- Include a section with the exact heading `## Rollback`.
- Include a `## Risks` section with at least two bullet points that start with `- `.

## Rules kept unchanged from `pr-structured`

- Under Testing
- list at least two checklist items written as `- [ ]` or `- [x]`
- Include a section with the exact heading `## Testing`
- Give the tracker ticket on its own line as `Ticket: <ID>`
- Include a section with the exact heading `## Summary`
- The first line must be a level-1 Markdown heading with the title, starting with `# `
- Keep the whole description to at most 120 words

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: Add rate limiting to the login endpoint

Labels: security, backend

Ticket: AUTH-207

Reviewer: @sam

## Rollback

- Revert changes to the login endpoint rate limiting configuration.

## Risks

- May cause legitimate users to be temporarily blocked if rate limits are too strict.
- Could lead to increased server load if not properly configured.

## Under Testing

- [ ] Test rate limiting with various user scenarios.
- [ ] Verify that rate limiting does not affect legitimate traffic.

## Testing

- Perform load testing to ensure rate limits are enforced correctly.
- Check that the system gracefully handles rate limit exceedance.

## Summary

This pull request adds rate limiting to the login endpoint to enhance security by preventing brute force attacks. It addresses ticket AUTH-207 and has been reviewed by @sam. The implementation includes thorough testing to ensure it does not negatively impact legitimate users. The description is kept concise at 120 words.
```
