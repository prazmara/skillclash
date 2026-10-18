---
name: release-announcement+keep-a-changelog
description: Merged skill that replaces `release-announcement` and `keep-a-changelog`. Use for any changelog entry.
---

# Merged skill: release-announcement + keep-a-changelog

This skill replaces `release-announcement` and `keep-a-changelog`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `release-announcement`

- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Mark incompatible changes with `BREAKING:` exactly.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Bullets describe the change only. No bullet may contain an @handle.
- Bullets are fragments: no bullet may end with a period.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`, followed immediately by a line with the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
- Credit every contributor by @handle and reference issues in parentheses as `(#<number>)`.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (March 2, 2026)
## [2.3.0] - 2026-03-02
Highlights: Added CSV export for reports and fixed a timezone bug in scheduled reports
BREAKING: the /v1/export endpoint was removed
Upgrade: migrate to the /v2/export endpoint before upgrading
### Added
- **CSV export for reports** (issue #412, by @dana)
### Fixed
- Timezone handling in scheduled reports (issue #398, by @lee)
```
