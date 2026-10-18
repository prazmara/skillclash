---
name: keep-a-changelog+release-announcement
description: Merged skill that replaces `keep-a-changelog` and `release-announcement`. Use for any changelog entry.
---

# Merged skill: keep-a-changelog + release-announcement

This skill replaces `keep-a-changelog` and `release-announcement`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Bullets describe the change only. No bullet may contain an @handle.
- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.

## Rules kept unchanged from `release-announcement`

- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Tell users what to do on a line that starts with `Upgrade: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Reference issues in parentheses as `(#<number>)` and credit every contributor by @handle.
- Each bullet must be a fragment and never end with a period, and every new feature name must be in bold with `**`.
