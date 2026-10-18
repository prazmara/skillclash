---
name: keep-a-changelog+release-announcement
description: Merged skill that replaces `keep-a-changelog` and `release-announcement`. Use for any changelog entry.
---

# Merged skill: keep-a-changelog + release-announcement

This skill replaces `keep-a-changelog` and `release-announcement`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`
- Flag incompatible changes with the exact marker `BREAKING:`
- Bullets describe the change only. No bullet may contain an @handle.
- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`

## Rules kept unchanged from `release-announcement`

- Release 2.3.0 (March 2, 2026)
- Highlights: reports can now be exported to CSV.
- **CSV export** for reports, thanks to @dana.
- BREAKING: the /v1/export endpoint was removed.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Fixed a timezone bug in scheduled reports, thanks to @lee (#1), and referenced issue (#2) in the changelog.
- To satisfy both rules, create a bullet point without a period at the end and ensure that any call to /v1/export is replaced with /v2/export before upgrading. For example: "Upgrade: replace calls to /v1/export with /v2/export before upgrading - Bullet point without a period at the end."
