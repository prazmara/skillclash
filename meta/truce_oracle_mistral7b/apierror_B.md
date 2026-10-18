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

- Write a JSON object response, enclosed in double quotes and with a single object containing a "Hint" key and a corresponding value that starts with "Hint:" and provides instructions for fixing the request. Ensure there are no extra characters or elements outside the JSON object format. Example: ``` "{\"Hint\": \"Hint: Ensure the API key is correctly formatted and included in the request header.\"}" ```

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "errorCode": "RATE_LIMIT_EXCEEDED",
  "details": ["The rate limit of 100 requests per minute has been exceeded."],
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium",
  "message": "The rate limit for POST /v1/payments has been exceeded.",
  "status": 429,
  "retryable": false,
  "docs": "https://example.com/api-errors/rate-limit-exceeded",
  "Hint": "Hint: Wait for the rate limit cooldown period before making further requests."
}
```
