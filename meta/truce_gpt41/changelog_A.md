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
- Bullets are fragments: no bullet may end with a period.

## Rules kept unchanged from `release-announcement`

- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The first two lines must be: (1) the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`, and (2) the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`. Both lines must appear in this order at the very start of the output.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (March 2, 2026)
## [2.3.0] - 2026-03-02
Highlights: This release introduces CSV export for reports and fixes a timezone bug in scheduled reports, but removes the /v1/export endpoint.
Upgrade: Review your integrations for the /v1/export endpoint and update to use the new CSV export feature.

### Added
- **CSV export for reports** (#412)

### Fixed
- timezone bug in scheduled reports (#398)

### Changed
BREAKING: removed the /v1/export endpoint
```
