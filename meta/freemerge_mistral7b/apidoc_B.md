<skill>
---
name: apidoc-integrator-guide-reference-card
description: Write REST endpoint documentation for external integrators as a compact reference card. Use for any API endpoint documentation.
---

# apidoc-integrator-guide-reference-card

Integrators build against the documentation without access to the source, so every parameter and every response status must be written down. The reference shows one card per endpoint in a narrow side panel, so each entry is short and carries the same few fields.

## Rules

- State the required permission on a line `Auth: <scope>`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- Show one example call on a line that starts with `$ curl `.
- The first line must be a level-3 Markdown heading with the method and path in backticks, for example ### `GET /v1/invoices/{id}`.
- Keep the whole entry to at most 90 words.
- State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.
- The first line must be the method and path alone in plain text with no Markdown, for example `GET /v1/invoices/{id}`.
- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.
- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Include an example request written as a shell line beginning with `$ curl `.
- Document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`.

## Example

Request: Write the documentation entry for the endpoint GET /v1/invoices/{id}: returns one invoice by ID. Requires the scope invoices:read. Path parameter id (string). Returns 200 with the invoice object, 403 if the scope is missing, 404 if the invoice does not exist. Available since API version 1.4.

Output:

```
### `GET /v1/invoices/{id}`

Returns a single invoice, including its line items, totals and payment state. Use this endpoint after listing invoices when the full object is needed.

Stability: stable
Content-Type: application/json

| Name | In | Type | Description |
|------|----|------|-------------|
| id | path | string | The identifier of the invoice to fetch |

Auth: invoices:read
Since: v1.4
Idempotent: yes

$ curl -H "Authorization: Bearer $TOKEN" https://api.example.com/v1/invoices/inv_123

Responses:
- 200: the invoice was found and is returned in full as a JSON object in the response body.
- 403: the access token is valid but does not carry the scope that this endpoint requires, so the request is refused.
- 404: no invoice with this identifier exists in the account that owns the access token.
```
</skill>
