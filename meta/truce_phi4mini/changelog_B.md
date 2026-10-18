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

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
## [2.3.0] - 2026-03-02

### Added
- Reports can now be exported to CSV (issue #412, by @dana).

### Fixed
- Fixed a timezone bug in scheduled reports (issue #398, by @lee).

### BREAKING
- The /v1/export endpoint was removed.
```
