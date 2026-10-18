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

- { "hint": "Hint: Check the request parameters and ensure they match the API documentation." }

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "status": 429,
  "errorCode": "RATE_LIMIT_EXCEEDED",
  "message": "The number of requests per minute has exceeded the allowed limit of 100. Please slow down your requests and try again later.",
  "details": [
    "You have exceeded the rate limit of 100 requests per minute for the POST /v1/payments endpoint.",
    "Retry after 60 seconds to avoid further rate limit violations."
  ],
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "high",
  "retryable": true,
  "docs": "https://docs.example.com/errors/RATE_LIMIT_EXCEEDED"
}
```
