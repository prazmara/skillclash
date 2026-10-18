---
name: keep-a-changelog+release-announcement
description: Merged skill that replaces `keep-a-changelog` and `release-announcement`. Use for any changelog entry.
---

# Merged skill: keep-a-changelog + release-announcement

This skill replaces `keep-a-changelog` and `release-announcement`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets describe the change only. No bullet may contain an @handle.
- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
- Bullets are fragments: no bullet may end with a period.

## Rules kept unchanged from `release-announcement`

- The first line must be the title `# Release <version> (<Month D, YYYY>)`
- Open with a one-sentence summary on a line that starts with `Highlights: `
- Credit every contributor by @handle
- Mark incompatible changes with `BREAKING:` exactly
- Tell users what to do on a line that starts with `Upgrade: `
- Put the name of each new feature in bold with `**`

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
## [2.3.0] - 2026-03-02

Highlights: This release includes CSV export for reports and fixes a timezone bug in scheduled reports.

### Added
- **CSV export for reports** (#412, @dana)

### Changed
- Fixed a timezone bug in scheduled reports (#398, @lee)

### Fixed
- None

### Removed
- BREAKING: The /v1/export endpoint was removed
```
