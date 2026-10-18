<skill>
---
name: apidoc-reference-card+apidoc-integrator-guide
description: Combined rules of `apidoc-reference-card` and `apidoc-integrator-guide`. Use for any REST endpoint documentation entry.
---

# Combined skill: apidoc-reference-card + apidoc-integrator-guide

Follow every rule below.

## Rules from `apidoc-reference-card`

- State the required permission on a line `Auth: <scope>`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- Show one example call on a line that starts with `$ curl `.
- The first line must be a level-3 Markdown heading with the method and path in backticks, for example ### `GET /v1/invoices/{id}`.
- Keep the whole entry to at most 90 words.
- State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.

## Rules from `apidoc-integrator-guide`

- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.
- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Include an example request written as a shell line beginning with `$ curl `.
- Document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`.

**Conflict Resolution**: If two rules conflict, the rule from `apidoc-reference-card` takes precedence. In particular, the rule "Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`" must be included, even if it adds length, and must be explicitly stated.

**Note**: The rule "The first line must be a level-3 Markdown heading with the method and path in backticks" from `apidoc-reference-card` takes precedence over any alternative formatting.
</skill>
