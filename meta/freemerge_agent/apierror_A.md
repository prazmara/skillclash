---
name: api-errors-internal-public
description: Write API error response bodies that internal services can parse and external developers can read. Use for any API error response.
---

# api-errors-internal-public

This skill merges `api-errors-internal` and `api-errors-public` and replaces both. Internal services parse error bodies automatically, so the body is strict machine-readable JSON. External developers read the same body while debugging, so it also explains itself.

Every rule of both skills is kept. Where two rules cannot both hold, `api-errors-internal` wins.

## Rules

- The reply must be exactly one JSON object and nothing else, so that it parses as JSON. Write no text before or after the object.
- Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys. This is the `api-errors-internal` rule. It overrides the `api-errors-public` rule that names the field `errorCode` and forbids snake_case keys, so `errorCode` must not appear. Every other key in this skill is a single lowercase word.
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
  "error_code": "rate_limit_exceeded",
  "message": "Rate limit of 100 requests per minute exceeded.",
  "status": 429,
  "retryable": true,
  "severity": "medium",
  "details": ["limit=100/min", "endpoint=POST /v1/payments"],
  "timestamp": "2026-03-02T10:15:00Z",
  "docs": "https://docs.example.com/errors/rate_limit_exceeded",
  "hint": "Hint: wait 60 seconds before retrying, or request a higher limit."
}
```
