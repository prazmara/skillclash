---
name: api-errors-public+api-errors-internal
description: Merged skill that replaces `api-errors-public` and `api-errors-internal`. Use for any JSON error response body.
---

# Merged skill: api-errors-public + api-errors-internal

This skill replaces `api-errors-public` and `api-errors-internal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `api-errors-public`

- Include a field `severity` with the value `low`, `medium` or `high`.
- Add a developer hint that starts with `Hint:` and says how to fix the request.
- Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.

## Rules kept unchanged from `api-errors-internal`

- Include a boolean field `retryable`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The combined rule is: "Include a human-readable sentence in the field `message` and ensure it explains the error for humans."
- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z` and a field `status` with an integer value, where the integer value is the HTTP status code.
- Include a field `details` that holds a non-empty list of specifics, and a field `docs` with an `https://` link to the error documentation. Ensure that `details` is not empty and `docs` is a valid URL.
