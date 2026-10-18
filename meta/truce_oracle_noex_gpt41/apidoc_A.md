---
name: apidoc-reference-card+apidoc-integrator-guide
description: Merged skill that replaces `apidoc-reference-card` and `apidoc-integrator-guide`. Use for any REST endpoint documentation entry.
---

# Merged skill: apidoc-reference-card + apidoc-integrator-guide

This skill replaces `apidoc-reference-card` and `apidoc-integrator-guide`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `apidoc-reference-card`

- The first line must be a level-3 Markdown heading with the method and path in backticks, for example ### `GET /v1/invoices/{id}`.
- State the required permission on a line `Auth: <scope>`.
- State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- Show one example call on a line that starts with `$ curl `.

## Rules kept unchanged from `apidoc-integrator-guide`

- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Keep the whole entry to at most 90 words, and document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`. Arrange the content carefully so both requirements are satisfied in the same output.
