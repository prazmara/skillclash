<skill>
---
name: api-errors
description: Write API error response bodies in the internal platform format for internal services and the public developer API format for external developers. Use for any API error response.
---

# api-errors

Internal services parse error bodies automatically, so the body is strict machine-readable JSON. External developers read error bodies while debugging, so the body explains itself.

## Rules

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Include a field `details` that holds a non-empty list of specifics.
- Add a developer hint that starts with `Hint:` and says how to fix the request.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.
- Name the machine-readable code field `error_code` (snake_case) for internal services, or `errorCode` (camelCase) for external developers. Never use both snake_case and camelCase keys.
- Explain the error for humans in the `message` field.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "error_code": "rate_limit_exceeded",
  "message": "Rate limit of 100 requests per minute exceeded.",
  "details": ["limit=100/min", "endpoint=POST /v1/payments"],
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium",
  "retryable": true,
  "status": 429,
  "docs": "https://docs.example.com/errors/rate_limit_exceeded"
}

Hint: wait 60 seconds before retrying, or request a higher limit.
```
</skill>
