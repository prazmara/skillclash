---
name: keep-a-changelog-release-announcement
description: Write changelog entries and release notes that strictly follow Keep a Changelog format and also provide a user-focused announcement. Use for any changelog or release notes.
---

# keep-a-changelog-release-announcement

This skill produces changelog entries that strictly follow Keep a Changelog format for tooling and integrators, and also provides a user-focused release announcement highlighting value and crediting contributors.

## Rules

- The output must contain two sections, in this order:
  1. The Keep a Changelog section, following all rules below.
  2. The Release Announcement section, following all rules below.
- **Keep a Changelog section:**
  - The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
  - Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
  - Flag incompatible changes with the exact marker `BREAKING:`.
  - Reference issues in parentheses as `(#<number>)`.
  - Bullets describe the change only. No bullet may contain an @handle.
  - Bullets are fragments: no bullet may end with a period.
- **Release Announcement section:**
  - The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`.
  - Open with a one-sentence summary on a line that starts with `Highlights: `.
  - Credit every contributor by @handle.
  - Mark incompatible changes with `BREAKING:` exactly.
  - Tell users what to do on a line that starts with `Upgrade: `.
  - Put the name of each new feature in bold with `**`.
- Where two rules cannot both hold, the rule from Keep a Changelog wins.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
## [2.3.0] - 2026-03-02

### Added
- CSV export for reports (#412)

### Fixed
- Timezone bug in scheduled reports (#398)

### Changed
- BREAKING: removed the /v1/export endpoint

# Release 2.3.0 (March 2, 2026)

Highlights: reports can now be exported to CSV.

- **CSV export** for reports, thanks to @dana.
- Fixed a timezone bug in scheduled reports, thanks to @lee.
- BREAKING: the /v1/export endpoint was removed.

Upgrade: replace calls to /v1/export with /v2/export before upgrading.
```
