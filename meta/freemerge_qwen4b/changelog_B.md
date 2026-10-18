---
name: release-changelog
description: Write release notes that are both user-friendly and tooling-compliant. Combines the clarity of release-announcement with the structure of keep-a-changelog. Use for any changelog or release notes.
---

# release-changelog

Release notes are read by end users and the community, so they highlight value and credit people. They are also parsed by tooling, so they must follow Keep a Changelog format strictly. This skill merges both goals: clear, human-readable content with structured, machine-readable formatting.

## Rules

- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets describe the change only. No bullet may contain an @handle.
- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Credit every contributor by @handle.
- Mark incompatible changes with `BREAKING:` exactly.
- Tell users what to do on a line that starts with `Upgrade: `.
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
