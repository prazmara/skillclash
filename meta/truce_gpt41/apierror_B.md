---
name: api-errors-public+api-errors-internal
description: Merged skill that replaces `api-errors-public` and `api-errors-internal`. Use for any JSON error response body.
---

# Merged skill: api-errors-public + api-errors-internal

This skill replaces `api-errors-public` and `api-errors-internal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `api-errors-public`

- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Add a developer hint that starts with `Hint:` and says how to fix the request.
- Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.
- Explain the error for humans in the `message` field.

## Rules kept unchanged from `api-errors-internal`

- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON, and must include a field `details` that holds a non-empty list of specifics.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium",
  "errorCode": "rateLimitExceeded",
  "message": "You have exceeded the allowed rate limit of 100 requests per minute for POST /v1/payments.",
  "retryable": true,
  "status": 429,
  "docs": "https://docs.example.com/errors/rate-limit-exceeded",
  "details": [
    "Request limit: 100 requests per minute.",
    "Endpoint: POST /v1/payments.",
    "Please wait before making additional requests."
  ],
  "Hint": "Reduce the frequency of your requests or implement exponential backoff to avoid hitting the rate limit."
}
```
