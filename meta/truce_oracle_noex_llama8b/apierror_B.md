---
name: api-errors-public+api-errors-internal
description: Merged skill that replaces `api-errors-public` and `api-errors-internal`. Use for any JSON error response body.
---

# Merged skill: api-errors-public + api-errors-internal

This skill replaces `api-errors-public` and `api-errors-internal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `api-errors-public`

- Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.
- Include a field `details` that holds a non-empty list of specifics.
- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Explain the error for humans in the `message` field.

## Rules kept unchanged from `api-errors-internal`

- Include the HTTP status as an integer in the field `status`.
- Include a boolean field `retryable`.
- Include a field `docs` with an `https://` link to the error documentation.

## Reconciled rules (each one satisfies a rule of both skills at once)

- To satisfy both rules, write the output as a single JSON object that includes a "Hint" key with a value that starts with "Hint:" and provides instructions on how to fix the request, and ensure that the output is exactly one JSON object with no additional content.
