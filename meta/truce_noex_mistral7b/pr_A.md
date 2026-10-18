---
name: pr-structured+pr-release-ready
description: Merged skill that replaces `pr-structured` and `pr-release-ready`. Use for any pull request description.
---

# Merged skill: pr-structured + pr-release-ready

This skill replaces `pr-structured` and `pr-release-ready`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `pr-structured`

- Include a section with the exact heading `## Testing`.
- Give the tracker ticket on its own line as `Ticket: <ID>`.
- Include a section with the exact heading `## Summary`.
- The first line must be a level-1 Markdown heading with the title, starting with `# `.

## Rules kept unchanged from `pr-release-ready`

- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- Include a section with the exact heading `## Rollback`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output as follows: - [ ] Checklist Item 1 - [ ] Checklist Item 2 Labels: ready-for-testing, release-ready
- Write a description of no more than 120 words, including a "## Risks" section with at least two bullet points starting with `- `, to ensure compliance with both the `pr-structured` and `pr-release-ready` rules.
