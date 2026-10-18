---
name: api-errors
description: Write API error response bodies for both internal and public developer APIs. Use for any API error response.
---

# api-errors

## Rules

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Name the machine-readable code field `error_code` (snake_case) for internal use and `errorCode` (camelCase) for public use. Use `error_code` for internal and `errorCode` for public.
- Include a human-readable sentence in the field `message`.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.
- For public errors, include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- For public errors, include a field `severity` with the value `low`, `medium`, or `high`.
- For public errors, include a field `details` that holds a non-empty list of specifics.
- For public errors, add a developer hint that starts with `Hint:` and says how to fix the request.

## Example

### Internal Error Response

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "error_code": "rate_limit_exceeded",
  "message": "Rate limit of 100 requests per minute exceeded.",
  "status": 429,
  "retryable": true,
  "docs": "https://docs.example.com/errors/rate_limit_exceeded"
}
```

### Public Error Response

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "errorCode": "RATE_LIMIT_EXCEEDED",
  "message": "Rate limit of 100 requests per minute exceeded.",
  "details": ["limit=100/min", "endpoint=POST /v1/payments"],
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium",
  "retryable": true,
  "status": 429,
  "docs": "https://docs.example.com/errors/rate_limit_exceeded",
  "Hint": "wait 60 seconds before retrying, or request a higher limit."
}
```
