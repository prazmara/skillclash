---
name: api-errors-internal+api-errors-public
description: Merged skill that replaces `api-errors-internal` and `api-errors-public`. Use for any JSON error response body.
---

# Merged skill: api-errors-internal + api-errors-public

This skill replaces `api-errors-internal` and `api-errors-public`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `api-errors-internal`

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.

## Rules kept unchanged from `api-errors-public`

- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Include a field `details` that holds a non-empty list of specifics.
- Add a developer hint that starts with `Hint:` and says how to fix the request.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Include a human-readable sentence in the `message` field for both `api-errors-internal` and `api-errors-public`, explaining the error clearly for humans.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "error_code": "rate_limit_exceeded",
  "status": 429,
  "severity": "medium",
  "timestamp": "2026-03-02T10:15:00Z",
  "retryable": false,
  "details": [
    "Exceeded the rate limit of 100 requests per minute."
  ],
  "message": "Rate limit exceeded. Please wait before making more requests.",
  "docs": "https://docs.example.com/errors/rate-limit-exceeded",
  "developer_hint": "Wait for the specified cooldown period before making additional requests."
}
```
