---
name: api-errors-internal+api-errors-public
description: One file that contains the skills `api-errors-internal` and `api-errors-public`. Use for any JSON error response body.
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
