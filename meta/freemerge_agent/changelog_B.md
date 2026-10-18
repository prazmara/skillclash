---
name: changelog-release-notes
description: Write release notes as a short announcement for users that also keeps the Keep a Changelog structure. Use for any changelog or release notes.
---

# changelog-release-notes

This skill merges `keep-a-changelog` and `release-announcement` and replaces both. Release notes are read by end users and by the community, so they highlight value, say how to upgrade and credit people. The same entry is parsed by tooling and read by integrators, so its body also follows Keep a Changelog.

Every rule of both skills is kept. Where two rules cannot both hold, `release-announcement` wins.

## Rules

- The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`. This is the `release-announcement` rule. It overrides the `keep-a-changelog` rule that the first line is the version heading `## [<version>] - <YYYY-MM-DD>`, so that heading is not written.
- Open the entry, directly after the title, with a one-sentence summary on a line that starts with `Highlights: `.
- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Bullets are fragments: no bullet may end with a period.
- Bullets describe the change only. No bullet may contain an @handle.
- Credit every contributor by @handle. Because handles may not appear in bullets, credit them on one plain line after the change groups, for example `Thanks to: @dana, @lee`. That line must not start with `- `.
- Put the name of each new feature in bold with `**`.
- Reference issues in parentheses as `(#<number>)`.
- Mark incompatible changes with the exact marker `BREAKING:`.
- Tell users what to do on a line that starts with `Upgrade: `.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (March 2, 2026)

Highlights: reports can now be exported to CSV.

### Added
- **CSV export** for reports (#412)

### Fixed
- Timezone bug in scheduled reports (#398)

### Changed
- BREAKING: removed the /v1/export endpoint

Upgrade: remove all calls to the /v1/export endpoint before upgrading.
Thanks to: @dana, @lee
```
