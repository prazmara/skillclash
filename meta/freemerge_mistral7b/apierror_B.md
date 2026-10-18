<skill>
---
name: api-errors
description: Write API error response bodies for both the public and internal platforms. Use for any API error response.
---

# api-errors

This skill provides rules for writing API error response bodies that are compatible with both the public and internal platforms.

## Rules

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Name the machine-readable code field `errorCode` (camelCase) for public consumption, and `error_code` (snake_case) for internal consumption.
- Include a human-readable sentence in the field `message`.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `details` that holds a non-empty list of specifics for public consumption.
- Add a developer hint that starts with `Hint:` and says how to fix the request for public consumption.
- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z` for public consumption.
- Include a field `severity` with the value `low`, `medium` or `high` for public consumption.
- Include a field `docs` with an `https://` link to the error documentation for internal consumption.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "errorCode": "RATE_LIMIT_EXCEEDED",
  "message": "Rate limit of 100 requests per minute exceeded.",
  "retryable": true,
  "status": 429,
  "details": ["limit=100/min", "endpoint=POST /v1/payments"],
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium",
  "error_code": "rate_limit_exceeded",
  "docs": "https://docs.example.com/errors/rate_limit_exceeded"

  Hint: wait 60 seconds before retrying, or request a higher limit.
}
```
</skill>
