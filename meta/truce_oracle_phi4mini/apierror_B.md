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

- "Add a developer hint that starts with `Hint:` and says how to fix the request, and ensure the reply is exactly one JSON object: `Hint: Check the request parameters and ensure they match the API documentation.` `{"error": "Invalid request parameters"}`"

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "errorCode": "RATE_LIMIT_EXCEEDED",
  "details": ["Rate limit exceeded for POST /v1/payments"],
  "timestamp": "2023-04-01T12:00:00Z",
  "severity": "high",
  "message": "You have exceeded the rate limit of 100 requests per minute for POST /v1/payments.",
  "status": 429,
  "retryable": true,
  "docs": "https://api.example.com/docs/rate-limits",
  "Hint": "Check the request parameters and ensure they match the API documentation."
}
```
