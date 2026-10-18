---
name: pr-release-ready+pr-structured
description: Merged skill that replaces `pr-release-ready` and `pr-structured`. Use for any pull request description.
---

# Merged skill: pr-release-ready + pr-structured

This skill replaces `pr-release-ready` and `pr-structured`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-release-ready`

- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- Include a section with the exact heading `## Rollback`.

## Rules kept unchanged from `pr-structured`

- Give the tracker ticket on its own line as `Ticket: <ID>`.
- Include a section with the exact heading `## Summary`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output as follows: `Labels: pr-release-ready, pr-structured Testing: - [ ] Item 1 - [ ] Item 2`
- Write the output in the following format: ``` PR: <title> ## Testing ``` Ensure the title is plain text and the "Testing" section is included as a subheading.
- Write a description of no more than 120 words, structured as follows: ``` ## Risks - Risk 1 - Risk 2 [Description (up to 120 words)] ``` Ensure that the description is concise and the "Risks" section contains at least two bullet points, each starting with `-`.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
Ticket: AUTH-207
Reviewers: @sam

PR: Add rate limiting to the login endpoint

## Summary

This pull request adds rate limiting to the login endpoint to prevent brute force attacks and improve system security.

## Risks
- Potential impact on legitimate users if rate limit is set too low
- Possible compatibility issues with existing clients that do not handle rate limiting

## Testing

- [ ] Unit tests for rate limiting functionality
- [ ] Integration tests for login endpoint with rate limiting

## Rollback

If the rate limiting implementation causes issues, the changes can be reverted by removing the rate limiting code and updating the login endpoint to its previous state.

## Labels
pr-release-ready, pr-structured
Testing: - [ ] Unit tests - [ ] Integration tests
```
