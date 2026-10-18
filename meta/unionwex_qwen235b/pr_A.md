---
name: pr-structured+pr-release-ready
description: Combined rules of `pr-structured` and `pr-release-ready`. Use for any pull request description.
---

# Combined skill: pr-structured + pr-release-ready

Follow every rule below.

## Rules from `pr-structured`

- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Include a section with the exact heading `## Testing`.
- Give the tracker ticket on its own line as `Ticket: <ID>`.
- Include a section with the exact heading `## Summary`.
- The first line must be a level-1 Markdown heading with the title, starting with `# `.
- Keep the whole description to at most 120 words.

## Rules from `pr-release-ready`

- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- Include a section with the exact heading `## Rollback`.
- Include a `## Risks` section with at least two bullet points that start with `- `.

If two rules cannot both hold, the rule from `pr-structured` wins.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add Rate Limiting to Login Endpoint

Ticket: AUTH-207  
Reviewers: @sam  
Labels: security, backend

## Summary  
Implemented rate limiting on the login endpoint to prevent brute-force attacks and protect user accounts. Uses a sliding window counter with Redis for tracking attempts per IP.

## Testing  
- [ ] Verify login attempts are blocked after 5 failures within 15 minutes  
- [ ] Confirm legitimate users can log in without issues under normal usage

## Risks  
- Legitimate users on shared IPs may be temporarily blocked  
- Incorrect Redis configuration could disable rate limiting entirely

## Rollback  
Revert the middleware addition to the login route and remove Redis rate-limiting logic.
```
