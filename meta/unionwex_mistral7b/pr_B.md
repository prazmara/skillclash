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
