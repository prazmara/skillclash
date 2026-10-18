---
name: pr-release-ready+pr-structured
description: Merged skill that replaces `pr-release-ready` and `pr-structured`. Use for any pull request description.
---

# Merged skill: pr-release-ready + pr-structured

This skill replaces `pr-release-ready` and `pr-structured`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-release-ready`

- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Put the ticket on a separate line in the form `Ticket: <ID>`.
- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- Include a `## Risks` section with at least two bullet points that start with `- `.

## Rules kept unchanged from `pr-structured`

- Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- Keep the whole description to at most 120 words.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Include a section with the exact heading `## Summary`, and on a line by itself, add `Reviewers: @handle`.
- Include a section with the exact heading `## Rollback` and a section with the exact heading `## Testing`.
