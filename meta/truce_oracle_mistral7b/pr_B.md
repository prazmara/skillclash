---
name: pr-release-ready+pr-structured
description: Merged skill that replaces `pr-release-ready` and `pr-structured`. Use for any pull request description.
---

# Merged skill: pr-release-ready + pr-structured

This skill replaces `pr-release-ready` and `pr-structured`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-release-ready`

- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- Include a section with the exact heading `## Rollback`.
- Name the reviewers on a line `Reviewers: @handle`.
- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Put the ticket on a separate line in the form `Ticket: <ID>`.

## Rules kept unchanged from `pr-structured`

- Include a section with the exact heading `## Summary`.
- Include a section with the exact heading `## Testing`.
- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write a description of no more than 120 words, structured as follows: ``` ## Risks - Risk 1 - Risk 2 [Description (up to 120 words)] ``` Ensure that the description is concise and the "Risks" section contains at least two bullet points, each starting with `-`.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: Add rate limiting to the login endpoint

## Summary

This pull request adds rate limiting to the login endpoint to prevent brute force attacks and improve the security of our application.

## Risks
- Incorrect implementation of rate limiting could potentially block legitimate users.
- Rate limiting may affect the performance of the login endpoint if not properly optimized.

## Testing
- [ ] Unit tests for rate limiting have been written and passed.
- [ ] Integration tests for the login endpoint have been run and passed.

## Rollback
In case of any issues, the rate limiting can be temporarily disabled by commenting out the relevant code in the login endpoint.

## Labels: security, backend
Reviewers: @sam

## Ticket: AUTH-207
```
