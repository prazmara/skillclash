<skill>
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

## Conflict Resolution

If two rules conflict, the rule from `pr-release-ready` takes precedence. Specifically, the rule "The first line must be plain text of the form `PR: <title>`" overrides the rule "The first line must be a level-1 Markdown heading with the title, starting with `# `".

## Word Limit

The entire pull request description must be no more than 120 words.

## Example

PR: Add multi-factor authentication to the admin portal

Labels: security, auth
Ticket: SEC-118
Reviewers: @jess

## Summary
Adds MFA to the admin portal to improve security. Prevents unauthorized access.

## Rollback
- Remove MFA flow and disable MFA endpoints.
- Revert authentication service config changes.

## Risks
- Increased login complexity may confuse users.
- Performance hit from extra auth checks.

## Testing
- [ ] Verify MFA is enforced during login.
- [ ] Confirm users are redirected to MFA challenge page without MFA.
</skill>
