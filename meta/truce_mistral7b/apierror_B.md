---
name: api-errors-public+api-errors-internal
description: Merged skill that replaces `api-errors-public` and `api-errors-internal`. Use for any JSON error response body.
---

# Merged skill: api-errors-public + api-errors-internal

This skill replaces `api-errors-public` and `api-errors-internal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `api-errors-public`

- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`
- Include a field `severity` with the value `low`, `medium` or `high`
- Include a field `details` that holds a non-empty list of specifics
- Add a developer hint that starts with `Hint:` and says how to fix the request

## Rules kept unchanged from `api-errors-internal`

- The reply must be exactly one JSON object and nothing else
- Name the machine-readable code field `error_code` (snake_case)
- Include a boolean field `retryable`
- Include the HTTP status as an integer in the field `status`
- Include a field `docs` with an `https://` link to the error documentation

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write an output that follows this format: `"The provided request encountered an internal error. (Error Code: [API_ERROR_CODE]) Please contact our support team for assistance. (Message: [HUMAN_READABLE_SENTENCE])"`, where `[API_ERROR_CODE]` is a unique error code for the internal error, and `[HUMAN_READABLE_SENTENCE]` is a human-readable explanation of the error. This format ensures that both rules from `api-errors-public` and `api-errors-internal` are satisfied.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium",
  "details": [
    "The rate limit of 100 requests per minute has been exceeded."
  ],
  "error_code": "RATE_LIMIT_EXCEEDED",
  "retryable": false,
  "status": 429,
  "docs": "https://example.com/docs/rate-limit-exceeded",
  "message": "The provided request encountered an internal error. (Error Code: RATE_LIMIT_EXCEEDED) Please contact our support team for assistance. (Message: The rate limit of 100 requests per minute has been exceeded.)"
}
```
