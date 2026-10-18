---
name: api-errors-internal+api-errors-public
description: Merged skill that replaces `api-errors-internal` and `api-errors-public`. Use for any JSON error response body.
---

# Merged skill: api-errors-internal + api-errors-public

This skill replaces `api-errors-internal` and `api-errors-public`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `api-errors-internal`

- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- Include the HTTP status as an integer in the field `status`.
- Include a boolean field `retryable`.
- Include a field `docs` with an `https://` link to the error documentation.
- Include a human-readable sentence in the field `message`.

## Rules kept unchanged from `api-errors-public`

- Include a field `details` that holds a non-empty list of specifics.
- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- "Create a JSON object with a 'hint' key containing a developer hint starting with 'Hint:', and ensure the JSON object is valid and contains no additional text."

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "error_code": "RATE_LIMIT_EXCEEDED",
  "status": 429,
  "retryable": true,
  "message": "You have exceeded the rate limit of 100 requests per minute on POST /v1/payments.",
  "details": [
    "Rate limit exceeded for POST /v1/payments"
  ],
  "timestamp": "2023-04-01T12:00:00Z",
  "severity": "high",
  "hint": "Hint: Check your request frequency and ensure you are not sending more than 100 requests per minute to POST /v1/payments."
}
```
