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

- Include a `## Risks` section with at least two bullet points that start with `- `, and keep the whole description to at most 120 words. Ensure both the `pr-release-ready` and `pr-structured` rules are satisfied in the same output.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: Add rate limiting to the login endpoint  
Ticket: AUTH-207  
Reviewers: @sam  
Labels: security, backend

## Summary
This PR introduces rate limiting on the login endpoint to prevent brute-force attacks and protect user accounts. The limit is set to 5 attempts per 15 minutes per IP address. Exceeding the limit returns a 429 status code.

## Testing
- [x] Verified rate limit blocks further login attempts after 5 failures
- [x] Confirmed legitimate logins are not affected under normal usage

## Risks
- Legitimate users on shared IPs might be rate-limited during high-traffic events
- Incorrect configuration could block valid authentication attempts

## Rollback
Revert the changes to the login route and remove the rate limiter middleware.
```
