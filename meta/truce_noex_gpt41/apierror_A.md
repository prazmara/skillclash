---
name: api-errors-internal+api-errors-public
description: Merged skill that replaces `api-errors-internal` and `api-errors-public`. Use for any JSON error response body.
---

# Merged skill: api-errors-internal + api-errors-public

This skill replaces `api-errors-internal` and `api-errors-public`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `api-errors-internal`

- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- Include a human-readable sentence in the field `message`.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.

## Rules kept unchanged from `api-errors-public`

- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Add a developer hint that starts with `Hint:` and says how to fix the request.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON, and it must include a field `details` that holds a non-empty list of specifics.
