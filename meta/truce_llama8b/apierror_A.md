---
name: api-errors-internal+api-errors-public
description: Merged skill that replaces `api-errors-internal` and `api-errors-public`. Use for any JSON error response body.
---

# Merged skill: api-errors-internal + api-errors-public

This skill replaces `api-errors-internal` and `api-errors-public`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `api-errors-internal`

- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- Include a boolean field `retryable`.
- Include a field `docs` with an `https://` link to the error documentation.

## Rules kept unchanged from `api-errors-public`

- Include a field `severity` with the value `low`, `medium` or `high`.
- Add a developer hint that starts with `Hint:` and says how to fix the request.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The output must be a single JSON object containing a field `details` with a non-empty list of specifics, and no other content.
- Include a human-readable sentence in the field `message` that explains the error for humans, starting with "An error occurred: ".
- Include a field `status` with an HTTP status as an integer, and a field `timestamp` with a UTC time in the form `YYYY-MM-DDTHH:MM:SSZ`, where `YYYY-MM-DDTHH:MM:SSZ` is a timestamp that includes the integer HTTP status as the seconds value, e.g., `2026-03-02T10:15:200Z`.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "error_code": "rate_limit_exceeded",
  "retryable": false,
  "severity": "high",
  "status": 429,
  "timestamp": "2024-07-26T14:30:429Z",
  "details": [
    {
      "field": "rate_limit",
      "limit": 100,
      "remaining": 0
    }
  ],
  "message": "An error occurred: You have exceeded the rate limit of 100 requests per minute.",
  "docs": "https://example.com/docs/rate-limits",
  "Hint:": "Please wait for 1 minute before making the next request or consider implementing exponential backoff."
}
```
