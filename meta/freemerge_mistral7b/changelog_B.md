<skill>
---
name: release-announcement-and-keep-a-changelog
description: Write release notes as a short announcement for users, following Keep a Changelog format. Use for any changelog or release notes.
---

# release-announcement-and-keep-a-changelog

Release notes are read by end users and by the community, so they highlight value and credit people, while following Keep a Changelog format.

## Rules

- The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`.
- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets describe the change only. No bullet may contain an @handle.
- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
- Bullets are fragments: no bullet may end with a period.
- Credit every contributor by @handle, but only in the `Highlights:` section.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (March 2, 2026)

Highlights: reports can now be exported to CSV, thanks to @dana.

## [2.3.0] - 2026-03-02

### Added
- CSV export for reports (#412)

### Fixed
- Timezone bug in scheduled reports (#398)

### Changed
- BREAKING: removed the /v1/export endpoint
```
</skill>
