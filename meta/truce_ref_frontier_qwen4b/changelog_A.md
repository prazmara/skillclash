<skill>
---
name: keep-a-changelog+release-announcement
description: Merged skill that replaces `keep-a-changelog` and `release-announcement`. Use for any changelog entry.
---

# Merged skill: keep-a-changelog + release-announcement

This skill replaces `keep-a-changelog` and `release-announcement`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Bullets describe the change only. No bullet may contain an @handle.
- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.

## Rules kept unchanged from `release-announcement`

- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Tell users what to do on a line that starts with `Upgrade: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Reference issues in parentheses as `(#<number>)` and credit every contributor by @handle.
- Each bullet must be a fragment and never end with a period, and every new feature name must be in bold with `**`.

## Fixed rule conflict: Bullets must not contain @handle, but contributors must be credited

To satisfy both:
- The contributor @handle must appear **only in the issue reference**, such as `(issue #412, by @dana)`, and **not in the bullet text**.
- The bullet itself must describe the change only and must not include any @handle outside of the issue reference.

## Fixed rule conflict: Upgrade instruction must be on a line starting with `Upgrade: `, not embedded in the highlights

To satisfy both:
- The upgrade instruction must appear **on a separate line starting with `Upgrade: `**, not within the highlights sentence.
- The highlights sentence must contain only feature and fix summaries, not upgrade guidance.

## Example

Request: Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.

Output:

```
## [2.3.0] - 2026-03-02

Highlights: Added CSV export for reports and fixed a timezone bug in scheduled reports.

### Added
- **CSV export for reports** (issue #412, by @dana)

### Fixed
- Timezone bug in scheduled reports (issue #398, by @lee)

BREAKING: The /v1/export endpoint was removed.

Upgrade: Users should upgrade to use the new report export format and avoid calling the deprecated /v1/export endpoint.
```
</skill>
