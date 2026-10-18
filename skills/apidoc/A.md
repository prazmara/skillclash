---
name: apidoc-reference-card
description: Write REST endpoint documentation as a compact reference card. Use for any API endpoint documentation.
---

# apidoc-reference-card

The reference shows one card per endpoint in a narrow side panel, so each entry is short and carries the same few fields.

## Rules

- State the required permission on a line `Auth: <scope>`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- Show one example call on a line that starts with `$ curl `.
- The first line must be a level-3 Markdown heading with the method and path in backticks, for example ### `GET /v1/invoices/{id}`.
- Keep the whole entry to at most 90 words.
- State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.

## Example

Request: Write the documentation entry for the endpoint GET /v1/invoices/{id}: returns one invoice by ID. Requires the scope invoices:read. Path parameter id (string). Returns 200 with the invoice object, 403 if the scope is missing, 404 if the invoice does not exist. Available since API version 1.4.

Output:

```
### `GET /v1/invoices/{id}`

Returns one invoice by ID.

Auth: invoices:read
Since: v1.4
Idempotent: yes

$ curl -H "Authorization: Bearer $TOKEN" https://api.example.com/v1/invoices/inv_123

Returns 404 if the invoice does not exist.
```
