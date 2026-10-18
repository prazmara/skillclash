---
name: api-errors-internal
description: Write API error response bodies in the internal platform format. Use for any API error response.
---

# api-errors-internal

Internal services parse error bodies automatically, so the body is strict machine-readable JSON.

## Rules

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- Include a human-readable sentence in the field `message`.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.

## Example

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
