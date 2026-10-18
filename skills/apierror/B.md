---
name: api-errors-public
description: Write API error response bodies for the public developer API. Use for any API error response.
---

# api-errors-public

External developers read error bodies while debugging, so the body explains itself.

## Rules

- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Include a field `details` that holds a non-empty list of specifics.
- Add a developer hint that starts with `Hint:` and says how to fix the request.
- Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.
- Explain the error for humans in the `message` field.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "errorCode": "RATE_LIMIT_EXCEEDED",
  "message": "Rate limit of 100 requests per minute exceeded.",
  "details": ["limit=100/min", "endpoint=POST /v1/payments"],
  "timestamp": "2026-03-02T10:15:00Z",
  "severity": "medium"
}

Hint: wait 60 seconds before retrying, or request a higher limit.
```
