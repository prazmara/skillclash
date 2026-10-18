---
name: pr-structured+pr-release-ready
description: Merged skill that replaces `pr-structured` and `pr-release-ready`. Use for any pull request description.
---

# Merged skill: pr-structured + pr-release-ready

This skill replaces `pr-structured` and `pr-release-ready`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-structured`

- Include a section with the exact heading `## Testing`.
- Give the tracker ticket on its own line as `Ticket: <ID>`.
- Include a section with the exact heading `## Summary`.
- The first line must be a level-1 Markdown heading with the title, starting with `# `.

## Rules kept unchanged from `pr-release-ready`

- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- Include a section with the exact heading `## Rollback`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output as follows: - [ ] Checklist Item 1 - [ ] Checklist Item 2 Labels: ready-for-testing, release-ready
- Write a description of no more than 120 words, including a "## Risks" section with at least two bullet points starting with `- `, to ensure compliance with both the `pr-structured` and `pr-release-ready` rules.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add Rate Limiting to Login Endpoint

## Ticket
AUTH-207

## Summary

Implement rate limiting for the login endpoint to prevent brute force attacks and improve system security.

## Testing

- Run unit tests for the login endpoint with and without rate limiting.
- Test the login endpoint with multiple concurrent requests to ensure rate limiting is working correctly.
- Verify that legitimate users are not affected by the rate limiting.

## Risks

- Improper implementation of rate limiting could potentially block legitimate users.
- The rate limiting mechanism may not be able to handle high traffic loads, leading to performance issues.

## Rollback

In case of any issues, revert the changes to the login endpoint and revert the rate limiting implementation.

- [ ] Checklist Item 1
- [ ] Checklist Item 2

Labels: ready-for-testing, release-ready

Reviewers: @sam
```
