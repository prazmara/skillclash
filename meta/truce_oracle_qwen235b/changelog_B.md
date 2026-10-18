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

- Credit every contributor by @handle in a dedicated "Contributors" section after the changelog. In the changelog, use bullets to describe changes only—no bullet may contain an @handle.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (March 2, 2026)  
Highlights: This release adds CSV export for reports, fixes a critical timezone bug, and removes the deprecated /v1/export endpoint.  
Upgrade: Enable CSV exports in your reports and update integrations to use /v2/export before upgrading.  

### Added  
- **CSV export for reports** enables downloading report data in CSV format (#412)  

### Fixed  
- Fixed a timezone bug in scheduled reports that caused incorrect execution times (#398)  

### Changed  
- BREAKING: Removed the `/v1/export` endpoint; use `/v2/export` for all export operations  

### Contributors  
Thanks to @dana and @lee for their contributions to this release.
```
