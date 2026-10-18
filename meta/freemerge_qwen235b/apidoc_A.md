---
name: apidoc-reference-card
description: Write REST endpoint documentation as a compact reference card for both side-panel display and external integrators. Use for any API endpoint documentation.
---

# apidoc-reference-card

This skill produces concise, complete API documentation suitable for both compact reference cards and external integrator use. It merges rules from both reference and integrator styles, prioritizing clarity, completeness, and consistency.

## Rules

- The first line must be a level-3 Markdown heading with the method and path in backticks, for example ### `GET /v1/invoices/{id}`.
- State the required permission on a line `Auth: <scope>`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- Show one example call on a line that starts with `$ curl `.
- Keep the whole entry to at most 90 words.
- State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.
- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.
- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`.

## Example

Request: Write the documentation entry for the endpoint GET /v1/invoices/{id}: returns one invoice by ID. Requires the scope invoices:read. Path parameter id (string). Returns 200 with the invoice object, 403 if the scope is missing, 404 if the invoice does not exist. Available since API version 1.4.

Output:

```
### `GET /v1/invoices/{id}`

Returns one invoice by ID.

Auth: invoices:read
Since: v1.4
Idempotent: yes
Stability: stable
Content-Type: application/json

| Name | In | Type | Description |
|------|----|------|-------------|
| id | path | string | The identifier of the invoice to fetch |

$ curl -H "Authorization: Bearer $TOKEN" https://api.example.com/v1/invoices/inv_123

Responses:
- 200: the invoice was found and is returned in full as a JSON object in the response body.
- 403: the access token is valid but does not carry the required scope.
- 404: no invoice with this identifier exists.
```
