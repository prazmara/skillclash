---
name: release-announcement+keep-a-changelog
description: Merged skill that replaces `release-announcement` and `keep-a-changelog`. Use for any changelog entry.
---

# Merged skill: release-announcement + keep-a-changelog

This skill replaces `release-announcement` and `keep-a-changelog`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `release-announcement`

- Release 2.3.0 (March 2, 2026)
- Highlights: reports can now be exported to CSV.
- **CSV export** for reports, thanks to @dana.
- BREAKING: the /v1/export endpoint was removed.

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`
- Flag incompatible changes with the exact marker `BREAKING:`
- Bullets describe the change only. No bullet may contain an @handle.
- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`

## Reconciled rules (each one satisfies a rule of both skills at once)

- "Include a fixed timezone bug announcement in the release notes, mentioning @lee, and reference any related issues in parentheses as `(#<number>)`."
- Replace calls to /v1/export with /v2/export and ensure that no bullet point in the changelog ends with a period.
