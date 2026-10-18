---
name: release-announcement+keep-a-changelog
description: Merged skill that replaces `release-announcement` and `keep-a-changelog`. Use for any changelog entry.
---

# Merged skill: release-announcement + keep-a-changelog

This skill replaces `release-announcement` and `keep-a-changelog`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `release-announcement`

- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Credit every contributor by @handle.
- Mark incompatible changes with `BREAKING:` exactly.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets are fragments: no bullet may end with a period.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Begin with the title line `# Release <version> (<Month D, YYYY>)`, immediately followed by the version heading line `## [<version>] - <YYYY-MM-DD>`. Use the exact literal markers, labels, and formats from both rules for each respective line.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (March 2, 2026)
## [2.3.0] - 2026-03-02

Highlights: Added CSV export for reports and fixed a timezone bug in scheduled reports; removed the /v1/export endpoint (BREAKING)

### Added
- **CSV export for reports** (#412, by @dana)

### Fixed
- Timezone bug in scheduled reports (#398, by @lee)

### Changed
- BREAKING: removed the /v1/export endpoint

Upgrade: Update your integrations to use the new export endpoints and formats
```
