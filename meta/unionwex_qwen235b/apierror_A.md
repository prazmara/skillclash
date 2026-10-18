---
name: api-errors-internal+api-errors-public
description: Combined rules of `api-errors-internal` and `api-errors-public`. Use for any JSON error response body.
---

# Combined skill: api-errors-internal + api-errors-public

Follow every rule below.

## Rules from `api-errors-internal`

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- Include a human-readable sentence in the field `message`.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.

## Rules from `api-errors-public`

- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Include a field `details` that holds a non-empty list of specifics.
- Add a developer hint that starts with `Hint:` and says how to fix the request.
- Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.
- Explain the error for humans in the `message` field.

If two rules cannot both hold, the rule from `api-errors-internal` wins.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "errorCode": "rate_limit_exceeded",
  "message": "You have exceeded the allowed number of requests per minute for this endpoint.",
  "status": 429,
  "retryable": true,
  "docs": "https://api.example.com/docs/errors/rate_limit_exceeded",
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium",
  "details": [
    "The rate limit for POST /v1/payments is 100 requests per minute.",
    "Current request count: 101 in the last 60 seconds."
  ],
  "error_code": "rate_limit_exceeded",
  "retryable": true,
  "docs": "https://api.example.com/docs/errors/rate_limit_exceeded",
  "Hint: Wait at least one minute before retrying, or contact support to request a higher rate limit."
}
```
