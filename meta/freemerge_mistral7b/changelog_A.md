<skill>
---
name: release-notes
description: Write release notes that follow both Keep a Changelog and release announcement formats. Use for any changelog or release notes.
---

# release-notes

Release notes are read by end users, the community, and tooling, so they highlight value, follow Keep a Changelog, and credit people.

## Rules

- The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`.
- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets describe the change only. No bullet may contain an @handle.
- The first line of each section must be the section heading, followed by a colon and a space.
- The first line of the changelog must be the version heading `## [<version>] - <YYYY-MM-DD>`.
- Bullets are fragments: no bullet may end with a period.
- Credit every contributor by @handle.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (March 2, 2026)

Highlights: reports can now be exported to CSV.

## [2.3.0] - 2026-03-02

### Added
- **CSV export** for reports (#412)

### Fixed
- Timezone bug in scheduled reports (#398)

### Changed
- BREAKING: removed the /v1/export endpoint

Upgrade: replace calls to /v1/export with /v2/export before upgrading.
```
</skill>
