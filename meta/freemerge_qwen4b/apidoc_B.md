---
name: apidoc-integrator-guide
description: Write REST endpoint documentation for external integrators. Use for any API endpoint documentation.
---

# apidoc-integrator-guide

Integrators build against the documentation without access to the source, so every parameter and every response status must be written down.

## Rules

- The first line must be the method and path alone in plain text with no Markdown, for example `GET /v1/invoices/{id}`.
- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.
- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Include an example request written as a shell line beginning with `$ curl `.
- Document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`.
- State the required permission on a line `Auth: <scope>`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.
- Keep the whole entry to at most 90 words.

## Example

Request: Write the documentation entry for the endpoint GET /v1/invoices/{id}: returns one invoice by ID. Requires the scope invoices:read. Path parameter id (string). Returns 200 with the invoice object, 403 if the scope is missing, 404 if the invoice does not exist. Available since API version 1.4.

Output:

```
GET /v1/invoices/{id}

Returns a single invoice, including its line items, totals and payment state. Use this endpoint after listing invoices when the full object is needed.

Stability: stable
Content-Type: application/json
Auth: invoices:read
Idempotent: yes
Since: v1.4

| Name | In | Type | Description |
|------|----|------|-------------|
| id | path | string | The identifier of the invoice to fetch |

$ curl -H "Authorization: Bearer $TOKEN" https://api.example.com/v1/invoices/inv_123

Responses:
- 200: the invoice was found and is returned in full as a JSON object in the response body.
- 403: the access token is valid but does not carry the scope that this endpoint requires, so the request is refused.
- 404: no invoice with this identifier exists in the account that owns the access token.
```
