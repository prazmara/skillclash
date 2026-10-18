---
name: api-errors-public+api-errors-internal
description: Combined rules of `api-errors-public` and `api-errors-internal`. Use for any JSON error response body.
---

# Combined skill: api-errors-public + api-errors-internal

Follow every rule below.

## Rules from `api-errors-public`

- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Include a field `details` that holds a non-empty list of specifics.
- Add a developer hint that starts with `Hint:` and says how to fix the request.
- Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.
- Explain the error for humans in the `message` field.

## Rules from `api-errors-internal`

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- Include a human-readable sentence in the field `message`.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.

If two rules cannot both hold, the rule from `api-errors-public` wins.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "timestamp": "2026-03-02T10:15:00Z",
  "status": 429,
  "errorCode": "RATE_LIMIT_EXCEEDED",
  "retryable": false,
  "severity": "high",
  "message": "You have exceeded the rate limit of 100 requests per minute for POST /v1/payments.",
  "details": [
    {
      "limit": 100,
      "remaining": 0,
      "reset": "2026-03-02T10:16:00Z"
    }
  ],
  "docs": "https://example.com/docs/rate-limits",
  "hint": "Hint: Try again after the rate limit resets at 2026-03-02T10:16:00Z or contact support for assistance."
}
```
