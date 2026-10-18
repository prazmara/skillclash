```markdown
<skill>
---
name: api-errors
description: Write API error response bodies for both public and internal APIs. Use for any API error response.
---

# api-errors

## Rules

- Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- Include a field `severity` with the value `low`, `medium` or `high`.
- Include a field `details` that holds a non-empty list of specifics.
- Add a developer hint that starts with `Hint:` and says how to fix the request.
- Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.
- Explain the error for humans in the `message` field.
- The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- Include a boolean field `retryable`.
- Include the HTTP status as an integer in the field `status`.
- Include a field `docs` with an `https://` link to the error documentation.

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
  "retryable": false,
  "status": 429,
  "docs": "https://docs.example.com/errors/rate_limit_exceeded"
}

Hint: wait 60 seconds before retrying, or request a higher limit.
```
</skill>
```

Note: The `retryable` field is set to `false` as per the `api-errors-public` skill, since it's generally not recommended to retry requests that exceeded a rate limit. If you want to allow retries, you can set it to `true`.
