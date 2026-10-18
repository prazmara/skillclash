<skill>
---
name: keep-a-changelog+release-announcement
description: Combined rules of `keep-a-changelog` and `release-announcement`. Use for any changelog entry.
---

# Combined skill: keep-a-changelog + release-announcement

Follow every rule below.

## Rules from `keep-a-changelog`

- Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues in parentheses as `(#<number>)`.
- Bullets describe the change only. No bullet may contain an @handle.
- The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.

## Rules from `release-announcement`

- The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`.
- Open with a one-sentence summary on a line that starts with `Highlights: `.
- Credit every contributor by @handle.
- Mark incompatible changes with `BREAKING:` exactly.
- Tell users what to do on a line that starts with `Upgrade: `.
- Put the name of each new feature in bold with `**`.

## Conflict Resolution

If two rules cannot both hold, the rule from `keep-a-changelog` takes precedence **only** when it directly contradicts a formatting or structural requirement in `release-announcement`. However, in cases where both rules are mutually incompatible, **both must be satisfied through explicit, consistent adaptation**:

- **The first line must be either**:
  - `## [<version>] - <YYYY-MM-DD>` (from `keep-a-changelog`), **OR**
  - `# Release <version> (<Month D, YYYY>)` (from `release-announcement`).
  - ✅ **Resolution**: The assistant must choose the format that allows all other rules to be satisfied. Since `keep-a-changelog` requires the version header in a specific format and `release-announcement` requires a title format, and both are essential, **the format from `keep-a-changelog` is prioritized** because it is the only one that allows proper grouping under `### Added`, `### Changed`, `### Fixed`, and is consistent with standard changelog conventions.  
  - ✅ **Therefore, the first line must be `## [<version>] - <YYYY-MM-DD>`**.

- **Issue references must be in parentheses**: `(#<number>)` — from `keep-a-changelog`.  
  ✅ This rule **must be enforced** and **cannot be compromised**, even if it conflicts with a `release-announcement` style.

- **No bullet may contain an @handle** — from `keep-a-changelog`.  
  ✅ This rule **must be enforced**. Any mention of a contributor must be done outside of bullets, e.g., in a separate "Contributors" section or in the Highlights.

- **"Put the name of each new feature in bold with `**`"** — from `release-announcement`.  
  ✅ This rule **must be satisfied**. New features must be described with bold formatting.  
  🔧 **Adaptation**: For each feature in `### Added`, the actual feature name must be in bold in the bullet.  
  Example: `**dark mode to the dashboard interface** (#501)`

- **"Open with a one-sentence summary on a line that starts with `Highlights: `."** — from `release-announcement`.  
  ❌ This conflicts with the `keep-a-changelog` requirement of starting with a version header.  
  ✅ **Resolution**: The `Highlights:` summary **must be included immediately after the version header**, as a standalone line, to satisfy `release-announcement`, while still starting with `## [<version>] - <YYYY-MM-DD>`.  
  Example:  
  `## [3.1.2] - 2026-04-15`  
  `Highlights: Dark mode and improved mobile responsiveness are now available.`

- **"Tell users what to do on a line that starts with `Upgrade: `."** — from `release-announcement`.  
  ✅ This must be included **only when there is a breaking change**.  
  🔧 **Adaptation**: If a `BREAKING:` change exists, the assistant **must** include a line starting with `Upgrade:` that explains what users should do.  
  Example: `Upgrade: Users must switch from legacy login to OAuth2 authentication.`

- **Credit every contributor by @handle** — from `release-announcement`.  
  ❌ This conflicts with the `keep-a-changelog` rule that forbids `@handle` in bullets.  
  ✅ **Resolution**: Contributors must be credited **in a separate line after the Highlights**, not in bullets.  
  Example: `Contributors: @michael, @sara`

## Final Rule Set (All Rules Enforced)

- The first line must be `## [<version>] - <YYYY-MM-DD>`.
- Immediately after the version header, include a single line starting with `Highlights: ` that summarizes the release in one sentence.
- Group changes under at least two of: `### Added`, `### Changed`, `### Fixed`.
- Flag incompatible changes with the exact marker `BREAKING:`.
- Reference issues as `(#<number>)` — never in parentheses without a number.
- Bullets describe the change only. No bullet may contain an @handle.
- Each new
