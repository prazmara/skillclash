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
