---
name: api-errors-internal+api-errors-public
description: Merged skill that replaces `api-errors-internal` and `api-errors-public`. Use for any JSON error response body.
---

# Merged skill: api-errors-internal + api-errors-public

This skill replaces `api-errors-internal` and `api-errors-public`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `api-errors-internal`

- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.

## Rules kept unchanged from `api-errors-public`

- Include a field `details` that holds a non-empty list of specifics.
- Add a developer hint that starts with `Hint:` and says how to fix the request.

## Reconciled rules (each one satisfies a rule of both skills at once)

- To satisfy both rules, create a JSON object with a `timestamp` field set to a UTC time in the form `2026-03-02T10:15:00Z`, and ensure the JSON object is valid and contains no additional fields or text.
- "Include a human-readable sentence in the field `message` that both explains the error for humans and can be used for internal error tracking."
- To satisfy both rules, include a boolean field `retryable` and a field `severity` with a value of `low`, `medium`, or `high` in the output. Ensure that the `retryable` field is set to `true` if the `severity` is `low` or `medium`, and set to `false` if the `severity` is `high`.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "error_code": "RATE_LIMIT_EXCEEDED",
  "status": 429,
  "docs": "https://api.example.com/docs/rate-limiting",
  "details": [
    "The request exceeded the rate limit of 100 requests per minute."
  ],
  "message": "You have exceeded the rate limit of 100 requests per minute. Please wait before sending more requests.",
  "retryable": true,
  "severity": "medium",
  "timestamp": "2023-04-01T12:00:00Z"
}
```
