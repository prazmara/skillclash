---
name: api-errors-internal-public
description: Write API error response bodies that external developers can read and internal services can parse. Use for any API error response.
---

# api-errors-internal-public

This skill merges `api-errors-internal` and `api-errors-public` and replaces both. External developers read error bodies while debugging, so the body explains itself. Internal services parse the same body automatically, so it is also strict machine-readable JSON.

Every rule of both skills is kept. Where two rules cannot both hold, `api-errors-public` wins.

## Rules

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON. Write no text before or after the object.
- Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys. This is the `api-errors-public` rule. It overrides the `api-errors-internal` rule that names the field `error_code` and forbids camelCase keys, so `error_code` must not appear. Every other key in this skill is a single lowercase word.
- Explain the error for humans with a readable sentence in the field `message`.
- Include the HTTP status as an integer in the field `status`.
- Include a boolean field `retryable`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Include a field `details` that holds a non-empty list of specifics.
- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `docs` with an `https://` link to the error documentation.
- Add a developer hint that starts with `Hint:` and says how to fix the request. Nothing may stand outside the JSON object, so the hint goes inside it as a string field `hint` whose value starts with `Hint:`.

## Example

Request: Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.

Output:

```
{
  "errorCode": "RATE_LIMIT_EXCEEDED",
  "message": "Rate limit of 100 requests per minute exceeded.",
  "status": 429,
  "retryable": true,
  "severity": "medium",
  "details": ["limit=100/min", "endpoint=POST /v1/payments"],
  "timestamp": "2026-03-02T10:15:00Z",
  "docs": "https://docs.example.com/errors/rate-limit-exceeded",
  "hint": "Hint: wait 60 seconds before retrying, or request a higher limit."
}
```
