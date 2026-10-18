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

- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Include a section with the exact heading `## Testing`.
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

## Summary  
Added rate limiting to the login endpoint to prevent brute-force attacks and protect user accounts.

## Testing  
- [ ] Verify login requests are limited to 5 attempts per minute per IP  
- [x] Confirm error response returns correct status code (429) when limit is exceeded

## Risks  
- Legitimate users behind shared IPs may be temporarily blocked  
- Incorrect configuration could impact login functionality during peak usage

## Rollback  
Revert the changes in `auth.middleware.rateLimit` and remove the rate limit rule from the login route.
```
