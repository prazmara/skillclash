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
# PR: Add rate limiting to the login endpoint

Labels: security, backend
Ticket: AUTH-207
Reviewers: @sam

## Summary
This PR adds rate limiting to the login endpoint to prevent brute-force attacks.

## Testing
- [ ] Test the rate limiting with a tool like Apache JMeter
- [x] Verify that the rate limiting is applied correctly for different user accounts

## Risks
- The rate limiting might block legitimate users if not configured correctly
- The rate limiting might not be effective against sophisticated attackers

## Rollback
If the rate limiting causes issues with legitimate users, we can adjust the configuration or remove it altogether.

## Risks
- The rate limiting might not be effective against sophisticated attackers
- The rate limiting might cause issues with our own automated testing infrastructure
```
