<skill>
---
name: api-errors-internal+api-errors-public
description: Combined rules of `api-errors-internal` and `api-errors-public`. Use for any JSON error response body.
---

# Combined skill: api-errors-internal + api-errors-public

Follow every rule below.

## Rules from `api-errors-internal`

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- Include a human-readable sentence in the field `message`.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.

## Rules from `api-errors-public`

- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Include a field `details` that holds a non-empty list of specifics.
- Add a developer hint that starts with `Hint:` and says how to fix the request.
- Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.
- Explain the error for humans in the `message` field.

## Conflict Resolution

If two rules conflict, the rule from `api-errors-internal` takes precedence over `api-errors-public` for the following fields:

- The machine-readable code field must be named `error_code` in **snake_case** (e.g., `"error_code": "EXPIRED_API_KEY"`), and **must not** use camelCase (`"errorCode"`). This overrides the `api-errors-public` rule that requires `errorCode` in camelCase.

## Example

{
  "error_code": "EXPIRED_API_KEY",
  "message": "The API key has expired and can no longer be used to access the resource.",
  "status": 401,
  "retryable": false,
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "high",
  "details": [
    "The API key provided in the request has expired.",
    "Authentication failed due to expired credentials."
  ],
  "docs": "https://docs.example.com/errors/EXPIRED_API_KEY",
  "hint": "Renew your API key from the developer console to resolve this issue."
}
</skill>
