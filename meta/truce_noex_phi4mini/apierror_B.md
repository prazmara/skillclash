---
name: api-errors-public+api-errors-internal
description: Merged skill that replaces `api-errors-public` and `api-errors-internal`. Use for any JSON error response body.
---

# Merged skill: api-errors-public + api-errors-internal

This skill replaces `api-errors-public` and `api-errors-internal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `api-errors-public`

- Include a field `details` that holds a non-empty list of specifics.
- Add a developer hint that starts with `Hint:` and says how to fix the request.

## Rules kept unchanged from `api-errors-internal`

- Include a field `docs` with an `https://` link to the error documentation.

## Reconciled rules (each one satisfies a rule of both skills at once)

- To satisfy both rules, include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z` and ensure the output is exactly one JSON object. The combined rule is: "Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z` and ensure the output is exactly one JSON object."
- "Include a human-readable sentence in the `message` field that explains the error for humans, ensuring that the explanation is clear and concise."
- To satisfy both rules, include a field `severity` with a value of `low`, `medium`, or `high`, and also include a boolean field `retryable`.
- Combine the `errorCode` and `status` fields into a single object with camelCase keys, where `errorCode` is a string and `status` is an integer. For example: `{ errorCode: "INVALID_INPUT", status: 400 }`.
