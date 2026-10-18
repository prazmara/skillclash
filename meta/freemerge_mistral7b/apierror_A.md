<skill>
---
name: api-errors
description: Write API error response bodies for both internal and public APIs. Use for any API error response.
---

# api-errors

This skill provides rules for writing API error response bodies that are compatible with both internal and public APIs.

## Rules

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Name the machine-readable code field `error_code` (snake_case) for internal use, and `errorCode` (camelCase) for public use.
- Include a human-readable sentence in the field `message`.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation for internal use.
- Include a field `details` that holds a non-empty list of specifics for public use.
- Add a developer hint that starts with `Hint:` and says how to fix the request for public use.
- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z` for public use.
- Include a field `severity` with the value `low`, `medium` or `high` for public use.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "error_code": "rate_limit_exceeded",
  "message": "Rate limit of 100 requests per minute exceeded.",
  "status": 429,
  "retryable": true,
  "docs": "https://docs.example.com/errors/rate_limit_exceeded",
  "details": ["limit=100/min", "endpoint=POST /v1/payments"],
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium",
  "Hint": "wait 60 seconds before retrying, or request a higher limit."
}
```
</skill>
