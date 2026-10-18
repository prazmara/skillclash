---
name: keep-a-changelog+release-announcement
description: Merged skill that replaces `keep-a-changelog` and `release-announcement`. Use for any changelog entry.
---

# Merged skill: keep-a-changelog + release-announcement

This skill replaces `keep-a-changelog` and `release-announcement`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets are fragments: no bullet may end with a period.

## Rules kept unchanged from `release-announcement`

- Open with a one-sentence summary on a line that starts with `Highlights: `
- Credit every contributor by @handle
- Put the name of each new feature in bold with `**`

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: ``` # Release [<version>] (<Month D, YYYY>) ## [<version>] - <YYYY-MM-DD> ```
- Write the output in the following format: ``` - Upgrade: [Your detailed instructions for users] [Bullet points describing the change only, without any @handle] ``` Ensure that no bullet point contains an @handle.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
# Release 2.3.0 (2026-03-02)

## [2.3.0] - 2026-03-02

Highlights:
- **CSV export for reports** (issue #412, by @dana)
- Fixed a timezone bug in scheduled reports (issue #398, by @lee)

- Upgrade: Users should update their scripts to use the new /v1/reports endpoint for CSV exports. The /v1/export endpoint has been removed. (BREAKING:)
```
