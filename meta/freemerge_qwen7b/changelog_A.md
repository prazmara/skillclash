---
name: combined-release-changelog
description: Write changelog entries in a format that combines the Keep a Changelog and Release Announcement styles. Use for any changelog or release notes.
---

# combined-release-changelog

This skill combines the formatting requirements of Keep a Changelog and Release Announcement to create a comprehensive changelog entry.

## Rules

- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Credit every contributor by @handle.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets describe the change only. No bullet may contain an @handle.
- Put the name of each new feature in bold with `**`.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
## [2.3.0] - 2026-03-02

Highlights: reports can now be exported to CSV.

### Added
- **CSV export** for reports (#412)

### Fixed
- Timezone bug in scheduled reports (#398)

### Changed
- BREAKING: removed the /v1/export endpoint

Upgrade: replace calls to /v1/export with /v2/export before upgrading.
```
