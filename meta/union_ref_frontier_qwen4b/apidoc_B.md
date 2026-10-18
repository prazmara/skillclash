<skill>
---
name: apidoc-integrator-guide+apidoc-reference-card
description: Combined rules of `apidoc-integrator-guide` and `apidoc-reference-card`. Use for any REST endpoint documentation entry.
---

# Combined skill: apidoc-integrator-guide + apidoc-reference-card

Follow every rule below.

## Rules from `apidoc-integrator-guide`

- The first line must be the method and path alone in plain text with no Markdown, for example `GET /v1/invoices/{id}`.
- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.
- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Include an example request written as a shell line beginning with `$ curl`.
- Document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`.

## Rules from `apidoc-reference-card`

- State the required permission on a line `Auth: <scope>`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- Show one example call on a line that starts with `$ curl`.
- The first line must be a level-3 Markdown heading with the method and path in backticks, for example ### `GET /v1/invoices/{id}`.
- Keep the whole entry to at most 90 words.
- State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.

## Resolution of Conflicts

If two rules conflict, the rule from `apidoc-integrator-guide` takes precedence. Specifically, the rule that the **first line must be the method and path alone in plain text with no Markdown** overrides the rule that the first line must be a level-3 Markdown heading. This ensures consistency with the core documentation format required by `apidoc-integrator-guide`.

## Corrected Example

`POST /v2/webhooks`

Stability: stable  
Content-Type: application/json  
Auth: webhooks:write  
Idempotent: no  
Since: v2.0  

| Name | In | Type | Description |
|------|----|------|-------------|
| url | body | string | The URL to which events will be sent. |
| event | body | string | The event type to subscribe to. |

$ curl -X POST https://api.example.com/v2/webhooks \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/webhook","event":"invoice.created"}'

Responses:  
- 201: Webhook registered successfully.  
- 400: Malformed URL.  
- 429: Rate limit exceeded.
</skill>
