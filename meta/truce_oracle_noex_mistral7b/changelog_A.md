---
name: keep-a-changelog+release-announcement
description: Merged skill that replaces `keep-a-changelog` and `release-announcement`. Use for any changelog entry.
---

# Merged skill: keep-a-changelog + release-announcement

This skill replaces `keep-a-changelog` and `release-announcement`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `keep-a-changelog`

- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets are fragments: no bullet may end with a period.
- Flag incompatible changes with the exact marker `BREAKING:`.

## Rules kept unchanged from `release-announcement`

- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the changelog in bullet points, where each bullet describes the change only, and include the contributor's @handle in parentheses after the change description when crediting them in the release announcement format: - Change: [Description of the change] (Contributor: @handle) - ... This way, the changelog follows the rule from the `keep-a-changelog` skill, and the release announcement rule is also satisfied by crediting every contributor with their @handle.
