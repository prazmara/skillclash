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

- Write a PR description that includes a `## Risks` section with at least two bullet points starting with `- `, and keep the description to at most 120 words, by placing the `## Risks` section at the end of the description, allowing the rest of the content to fit within the 120-word limit.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: Add rate limiting to the login endpoint

## Summary
This PR adds rate limiting to the login endpoint to prevent brute-force attacks.

## Rollback
In case of issues, we can revert the changes by removing the rate limiting middleware.

Reviewers: @sam
Labels: security, backend
Ticket: AUTH-207

## Testing
- [ ] Test the login endpoint with a high number of requests to verify rate limiting.
- [x] Verify that the rate limiting is correctly configured.

## Risks
- The rate limiting might impact legitimate users with slow internet connections.
- The rate limiting configuration might need to be adjusted based on production data.
```
