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

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "error_code": "rate_limit_exceeded",
  "message": "You have exceeded the rate limit of 100 requests per minute for POST /v1/payments.",
  "retryable": true,
  "status": 429,
  "docs": "https://docs.example.com/errors/rate_limit_exceeded",
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium",
  "details": [
    "The rate limit for POST /v1/payments is 100 requests per minute.",
    "Further requests will be rejected until the rate limit window resets.",
    "Consider implementing exponential backoff or request throttling."
  ],
  "Hint": "Reduce the frequency of your requests to stay within the allowed rate limit, or wait until the next minute before retrying."
}
```
