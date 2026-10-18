---
name: keep-a-changelog+release-announcement
description: Combined rules of `keep-a-changelog` and `release-announcement`. Use for any changelog entry.
---

# Combined skill: keep-a-changelog + release-announcement

Follow every rule below.

## Rules from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets describe the change only. No bullet may contain an @handle.
- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
- Bullets are fragments: no bullet may end with a period.

## Rules from `release-announcement`

- The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`.
- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Credit every contributor by @handle.
- Mark incompatible changes with `BREAKING:` exactly.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.

If two rules cannot both hold, the rule from `keep-a-changelog` wins.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
## [2.3.0] - 2026-03-02
Highlights: Added CSV export for reports and fixed a critical timezone bug in scheduled reports.
Upgrade: Migrate from /v1/export to /v2/export before upgrading.
### Added
- **CSV export for reports** (issue #412, by @dana)
### Fixed
- Timezone handling in scheduled reports (issue #398, by @lee)
### Changed
- BREAKING: Removed the /v1/export endpoint
```
