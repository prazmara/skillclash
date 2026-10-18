---
name: pr-release-ready+pr-structured
description: Combined rules of `pr-release-ready` and `pr-structured`. Use for any pull request description.
---

# Combined skill: pr-release-ready + pr-structured

Follow every rule below.

## Rules from `pr-release-ready`

- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- Include a section with the exact heading `## Rollback`.
- Include a `## Risks` section with at least two bullet points that start with `- `.

## Rules from `pr-structured`

- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Include a section with the exact heading `## Testing`.
- Give the tracker ticket on its own line as `Ticket: <ID>`.
- Include a section with the exact heading `## Summary`.
- The first line must be a level-1 Markdown heading with the title, starting with `# `.
- Keep the whole description to at most 120 words.

If two rules cannot both hold, the rule from `pr-release-ready` wins.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
PR: Add rate limiting to the login endpoint  
Labels: security, backend  
Ticket: AUTH-207  
Reviewers: @sam

## Summary

This PR introduces rate limiting to the login endpoint to mitigate brute-force attacks. The implementation restricts the number of login attempts per IP within a set timeframe, enhancing security.

## Risks

- May inadvertently block legitimate users if thresholds are too strict.
- Could introduce performance overhead or conflicts with existing middleware.

## Rollback

Revert the rate limiting middleware and restore the previous login endpoint logic.

## Testing

- [ ] Attempt multiple logins from the same IP to verify rate limiting triggers.
- [ ] Confirm legitimate users can still log in under normal conditions.
```
