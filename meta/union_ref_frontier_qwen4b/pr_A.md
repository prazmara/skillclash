<skill>
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

## Rules from `pr-release-ready`

- List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- Put the ticket on a separate line in the form `Ticket: <ID>`.
- Name the reviewers on a line `Reviewers: @handle`.
- The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- Include a section with the exact heading `## Rollback`.
- Include a `## Risks` section with at least two bullet points that start with `- `.

## Conflict Resolution
When a rule from `pr-structured` and `pr-release-ready` conflict, the rule from `pr-structured` takes precedence. Specifically, the first line must be a level-1 Markdown heading (`# `) as required by `pr-structured`, and the `PR: <title>` format from `pr-release-ready` must be replaced with `# <title>`.

## Example
# Add user consent tracking for data collection  
Ticket: PRIV-550  
Reviewers: @kate  
Labels: compliance, security  

## Summary  
Adds user consent tracking to monitor data collection activities, ensuring compliance with privacy regulations.  

## Testing  
- [ ] Unit tests pass for consent flow  
- [ ] End-to-end tests verify user consent UI and data logging  

## Rollback  
Revert consent tracking changes and remove all related code.  

## Risks  
- May impact user experience if consent prompts are too frequent.  
- Could introduce latency in data collection if tracking overhead increases.
</skill>
