---
name: changelog-release-notes
description: Write changelog entries in Keep a Changelog format that also work as a short release announcement for users. Use for any changelog or release notes.
---

# changelog-release-notes

This skill merges `keep-a-changelog` and `release-announcement` and replaces both. The changelog is parsed by tooling and read by integrators, so it follows Keep a Changelog strictly. The same entry is read by end users and by the community, so it also highlights value, says how to upgrade and credits people.

Every rule of both skills is kept. Where two rules cannot both hold, `keep-a-changelog` wins.

## Rules

- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`. This is the `keep-a-changelog` rule. It overrides the `release-announcement` rule that the first line is the title `# Release <version> (<Month D, YYYY>)`, so that title is not written.
- Open the entry, directly after the heading, with a one-sentence summary on a line that starts with `Highlights: `.
- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Bullets are fragments: no bullet may end with a period.
- Bullets describe the change only. No bullet may contain an @handle.
- Credit every contributor by @handle. Because handles may not appear in bullets, credit them on one plain line after the change groups, for example `Thanks to: @dana, @lee`. That line must not start with `- `.
- Put the name of each new feature in bold with `**`.
- Reference issues in parentheses as `(#<number>)`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Tell users what to do on a line that starts with `Upgrade: `.

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

Upgrade: remove all calls to the /v1/export endpoint before upgrading.
Thanks to: @dana, @lee
```
