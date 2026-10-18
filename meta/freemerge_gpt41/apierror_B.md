---
name: api-errors-merged
description: Write API error response bodies for both public developer and internal platform APIs, merging all rules. Use for any API error response.
---

# api-errors-merged

This skill merges the requirements for public developer API and internal platform API error responses. The response body is informative for external developers and machine-readable for internal services.

## Rules

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Include a field `details` that holds a non-empty list of specifics.
- Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.
- Explain the error for humans in the `message` field.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.
- Add a developer hint that starts with `Hint:` and says how to fix the request. The hint must be provided after the JSON object, not inside it.

## Example

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
  "docs": "https://docs.example.com/errors/rate_limit_exceeded"
}

Hint: wait 60 seconds before retrying, or request a higher limit.
```
