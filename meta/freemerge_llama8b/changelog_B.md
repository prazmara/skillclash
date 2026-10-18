<skill>
---
name: release-announcement
description: Write release notes as a short announcement for users. Use for any changelog or release notes.
---

# release-announcement

Release notes are read by end users and by the community, so they highlight value and credit people.

## Rules

- The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`.
- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Credit every contributor by @handle in the description of the change.
- Mark incompatible changes with `BREAKING:` exactly.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.
- Bullets describe the change only. No bullet may contain an @handle.
- Bullets are fragments: no bullet may end with a period.
- Reference issues in parentheses as `(#<number>)`.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (March 2, 2026)

Highlights: reports can now be exported to CSV.

### Added
- **CSV export** for reports (#412, thanks to @dana).
- **Fixed a timezone bug** in scheduled reports (#398, thanks to @lee).

### Changed
- BREAKING: the /v1/export endpoint was removed.

Upgrade: replace calls to /v1/export with /v2/export before upgrading.
```
