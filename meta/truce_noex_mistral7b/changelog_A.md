---
name: keep-a-changelog+release-announcement
description: Merged skill that replaces `keep-a-changelog` and `release-announcement`. Use for any changelog entry.
---

# Merged skill: keep-a-changelog + release-announcement

This skill replaces `keep-a-changelog` and `release-announcement`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets are fragments: no bullet may end with a period.

## Rules kept unchanged from `release-announcement`

- Open with a one-sentence summary on a line that starts with `Highlights: `
- Credit every contributor by @handle
- Put the name of each new feature in bold with `**`

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: ``` # Release [<version>] (<Month D, YYYY>) ## [<version>] - <YYYY-MM-DD> ```
- Write the output in the following format: ``` - Upgrade: [Your detailed instructions for users] [Bullet points describing the change only, without any @handle] ``` Ensure that no bullet point contains an @handle.
