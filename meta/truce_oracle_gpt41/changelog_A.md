---
name: keep-a-changelog+release-announcement
description: Merged skill that replaces `keep-a-changelog` and `release-announcement`. Use for any changelog entry.
---

# Merged skill: keep-a-changelog + release-announcement

This skill replaces `keep-a-changelog` and `release-announcement`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `keep-a-changelog`

- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets are fragments: no bullet may end with a period.
- Flag incompatible changes with the exact marker `BREAKING:`.

## Rules kept unchanged from `release-announcement`

- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- List all changes as bullets that describe the change only, with no @handle in any bullet. After the bullet list, credit every contributor by @handle.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
## [2.3.0] - 2026-03-02

Highlights: CSV export for reports is now available and a timezone bug in scheduled reports is fixed
Upgrade: Review the removal of the /v1/export endpoint before upgrading

### Added
- **CSV export for reports** (#412)

### Fixed
- Timezone bug in scheduled reports (#398)

### Changed
- BREAKING: /v1/export endpoint was removed

Contributors: @dana, @lee
```
