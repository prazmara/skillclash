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

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "errorCode": "RATE_LIMIT_EXCEEDED",
  "details": ["Exceeded rate limit of 100 requests per minute on POST /v1/payments"],
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "high",
  "message": "Rate limit exceeded for POST /v1/payments. Please try again after 1 minute.",
  "status": 429,
  "retryable": false,
  "docs": "https://example.com/docs/rate-limits",
  "Hint": "Hint: Try again after 1 minute or consider implementing exponential backoff to avoid hitting the rate limit in the future."
}
```
