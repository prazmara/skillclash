---
name: pr-structured+pr-release-ready
description: Merged skill that replaces `pr-structured` and `pr-release-ready`. Use for any pull request description.
---

# Merged skill: pr-structured + pr-release-ready

This skill replaces `pr-structured` and `pr-release-ready`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-structured`

- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Give the tracker ticket on its own line as `Ticket: <ID>`.
- The first line must be a level-1 Markdown heading with the title, starting with `# `.
- Keep the whole description to at most 120 words.

## Rules kept unchanged from `pr-release-ready`

- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Include a `## Risks` section with at least two bullet points that start with `- `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Include a section with the exact heading `## Summary`, and name the reviewers on a line `Reviewers: @handle`.
- Include a section with the exact heading `## Testing` and another section with the exact heading `## Rollback`.

## Example

Request: Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.

Output:

```
# Add Rate Limiting to Login Endpoint

Ticket: AUTH-207  
Reviewers: @sam  
Labels: security, backend

## Summary  
Adds rate limiting to the login endpoint to prevent brute force attacks.  

## Testing  
- [ ] Unit tests pass for login endpoint under rate limiting  
- [ ] Integration tests verify rate limit enforcement after 5 failed attempts  

## Risks  
- Rate limiting could impact legitimate users during high traffic periods  
- Misconfiguration might lead to unintended blocking of valid login requests  

## Rollback  
- Remove rate limiting configuration from login endpoint  
- Restore previous login endpoint behavior without rate limiting
```
