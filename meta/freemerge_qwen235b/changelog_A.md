---
name: release-notes-combined
description: Write comprehensive release notes that follow Keep a Changelog format and include user-friendly announcements with contributor credits. Use for any changelog or release notes.
---

# release-notes-combined

Release notes must satisfy both tooling requirements and user communication needs. They follow Keep a Changelog format strictly, while also delivering a clear, value-oriented message to users and crediting contributors.

## Rules

- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`. (From `keep-a-changelog`)
- Immediately after the version heading, include a title line: `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`. (From `release-announcement`)
- After the title, open with a one-sentence summary on a line that starts with `Highlights: `. (From `release-announcement`)
- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`. (From `keep-a-changelog`)
- Bullets describe the change only. No bullet may contain an @handle. (From `keep-a-changelog`)
- Credit every contributor by @handle in a separate sentence following the bullet or in the bullet's trailing clause, provided it does not violate the prior rule. If needed, add a sentence after the changelog section crediting contributors. (From `release-announcement`, adapted)
- Flag incompatible changes with the exact marker `BREAKING:`. (Both, `keep-a-changelog` wins on phrasing)
- Reference issues in parentheses as `(#<number>)`. (From `keep-a-changelog`)
- Bullets are fragments: no bullet may end with a period. (From `keep-a-changelog`)
- Put the name of each new feature in bold with `**`. (From `release-announcement`)
- Tell users what to do on a line that starts with `Upgrade: `. (From `release-announcement`)

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
## [2.3.0] - 2026-03-02
# Release 2.3.0 (March 2, 2026)

Highlights: reports can now be exported to CSV.

### Added
- **CSV export** for reports (#412)

### Fixed
- Timezone bug in scheduled reports (#398)

### Changed
- BREAKING: removed the /v1/export endpoint

Thanks to @dana and @lee for their contributions.

Upgrade: replace calls to /v1/export with /v2/export before upgrading.
```
