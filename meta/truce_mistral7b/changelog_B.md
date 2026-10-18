---
name: release-announcement+keep-a-changelog
description: Merged skill that replaces `release-announcement` and `keep-a-changelog`. Use for any changelog entry.
---

# Merged skill: release-announcement + keep-a-changelog

This skill replaces `release-announcement` and `keep-a-changelog`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `release-announcement`

- Open with a one-sentence summary on a line that starts with `Highlights: `
- Credit every contributor by @handle
- Mark incompatible changes with `BREAKING:` exactly
- Put the name of each new feature in bold with `**`

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Bullets are fragments: no bullet may end with a period.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: ``` # Release <version> (<Month D, YYYY>) ## [<version>] - <YYYY-MM-DD> ``` Replace `<version>` with the version number and `<Month D, YYYY>` with the release date in the format "Month Day, Year". Replace `<YYYY-MM-DD>` with the date in the format "Year-Month-Day".
- Write the output in the following format: ``` Upgrade: - Bullet 1: [Description of change] (No @handle is included) - Bullet 2: [Description of change] (No @handle is included) - ... ``` This way, the first line starts with "Upgrade:", and each subsequent line starts with a bullet, adhering to both rules.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (March 02, 2026)

## [2.3.0] - 2026-03-02

### Added
- **CSV export for reports** (issue #412, by @dana)

### Fixed
- Timezone bug in scheduled reports (issue #398, by @lee)

### Breaking
- The /v1/export endpoint was removed

### Upgrade
- Removed the /v1/export endpoint
- Fixed a timezone bug in scheduled reports
- Added CSV export for reports
```
