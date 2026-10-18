---
name: release-announcement+keep-a-changelog
description: Merged skill that replaces `release-announcement` and `keep-a-changelog`. Use for any changelog entry.
---

# Merged skill: release-announcement + keep-a-changelog

This skill replaces `release-announcement` and `keep-a-changelog`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `release-announcement`

- The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`.
- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.
- Mark incompatible changes with `BREAKING:` exactly.

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets are fragments: no bullet may end with a period.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the changelog in the following format: - Change: [Description of the change] - Credit: [Contributor's handle] This way, each bullet describes the change only (as per the `keep-a-changelog` rule), and the contributor's handle is included (as per the `release-announcement` rule).

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (March 2, 2026)

Highlights:
- CSV export for reports added (issue #412)
- Timezone bug in scheduled reports fixed (issue #398)

Upgrade: Please update to the latest version to benefit from these improvements.

### Added
- **CSV export for reports** (issue #412, by @dana)

### Fixed
- Timezone bug in scheduled reports (issue #398, by @lee)

### Changed
- **Removed /v1/export endpoint** (BREAKING:)

- Change: CSV export for reports added
- Credit: @dana

- Change: Timezone bug in scheduled reports fixed
- Credit: @lee

- Change: /v1/export endpoint removed (BREAKING:)
```
