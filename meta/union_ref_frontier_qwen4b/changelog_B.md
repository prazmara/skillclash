<skill>
---
name: release-announcement+keep-a-changelog
description: Combined rules of `release-announcement` and `keep-a-changelog`. Use for any changelog entry.
---

# Combined skill: release-announcement + keep-a-changelog

Follow every rule below. When conflicts arise, the rule from `release-announcement` takes precedence.

## Rules from `release-announcement`

- The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`.
- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Credit every contributor by @handle.
- Mark incompatible changes with `BREAKING:` exactly.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.

## Rules from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets describe the change only. No bullet may contain an @handle.
- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
- Bullets are fragments: no bullet may end with a period.

## Conflict Resolution

If a rule from `release-announcement` and a rule from `keep-a-changelog` conflict, the `release-announcement` rule wins. However, where both rules apply and are compatible, both must be satisfied.

Specifically:
- The **first line** must follow `# Release <version> (<Month D, YYYY>)` (from `release-announcement`) **and** the version heading `## [<version>] - <YYYY-MM-DD>` (from `keep-a-changelog`) — but **only if both are required**. Since `release-announcement` takes precedence, the first line must be `# Release <version> (<Month D, YYYY>)`.
- The **bullets must be fragments without periods** and must **not contain @handle** — this is enforced by `keep-a-changelog`, and must be satisfied even when `release-announcement` is used.
- **Issue references must be in the form `(#<number>)`** — this is required by `keep-a-changelog` and must be included in all bullet points.
- **Contributor credits (@handle)** must appear only in the `Highlights:` sentence and **not in bullets** — this satisfies `release-announcement` without violating `keep-a-changelog`'s bullet rule.
- **Grouping under `### Added`, `### Changed`, `### Fixed`** must occur — this is required by `keep-a-changelog`. The `release-announcement` rule does not override this.
- **Incompatible changes must be marked with `BREAKING:` exactly** — this is required by both rules and must be used consistently.
- **Upgrade instructions must start with `Upgrade: `** — this is required by `release-announcement` and must appear after a `BREAKING:` change.

## Example (Corrected and Fully Compliant)

# Release 2.9.7 (February 12, 2026)

Highlights: This release adds support for custom data fields and improves dashboard loading performance, with a breaking change to the /v1/fields endpoint.

### Added
**Added support for custom data fields** (#389, by @nathan)

### Changed
Improved loading speed for dashboard pages (#405, by @amanda)

BREAKING: the /v1/fields endpoint is no longer functional.  
Upgrade: Migrate any usage of the /v1/fields endpoint to the new /v2/fields endpoint.

</skill>
