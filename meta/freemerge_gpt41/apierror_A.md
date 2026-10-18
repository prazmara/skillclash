---
name: api-errors-merged
description: Write API error response bodies for both internal and public APIs, combining all required fields and formats. Use for any API error response.
---

# api-errors-merged

This skill merges the requirements for both internal platform and public developer API error responses. The response body must be strict machine-readable JSON, including all required fields from both specifications.

## Rules

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- Include a human-readable sentence in the field `message`.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.
- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Include a field `details` that holds a non-empty list of specifics.
- Add a developer hint that starts with `Hint:` and says how to fix the request, as a separate line after the JSON object.
- Where two rules cannot both hold, the rule from `api-errors-internal` wins (e.g., use `error_code` in snake_case, not `errorCode` in camelCase).

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
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium",
  "details": ["limit=100/min", "endpoint=POST /v1/payments"]
}

Hint: wait 60 seconds before retrying, or request a higher limit.
```
