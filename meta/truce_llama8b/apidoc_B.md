---
name: apidoc-integrator-guide+apidoc-reference-card
description: Merged skill that replaces `apidoc-integrator-guide` and `apidoc-reference-card`. Use for any REST endpoint documentation entry.
---

# Merged skill: apidoc-integrator-guide + apidoc-reference-card

This skill replaces `apidoc-integrator-guide` and `apidoc-reference-card`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `apidoc-integrator-guide`

- The first line must be the method and path alone in plain text with no Markdown, for example `GET /v1/invoices/{id}`.
- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.
- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Include an example request written as a shell line beginning with `$ curl `.
- Document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`.

## Rules kept unchanged from `apidoc-reference-card`

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
Stability: stable
Content-Type: application/json

| Name | In | Type | Description |
| --- | --- | --- | --- |
| id | path | string | Invoice ID |

Auth: invoices:read
Idempotent: no
Since: v1.4

$ curl -X GET 'https://api.example.com/v1/invoices/{id}'

Responses:
- 200: Invoice object
- 403: Missing scope
- 404: Invoice not found
```
