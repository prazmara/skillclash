---
name: apidoc-card-integrator
description: Write REST endpoint documentation as a compact reference card that external integrators can build against. Use for any API endpoint documentation.
---

# apidoc-card-integrator

This skill merges `apidoc-reference-card` and `apidoc-integrator-guide` and replaces both. The reference shows one card per endpoint in a narrow side panel, so each entry is short and carries the same fields. Integrators build against the entry without access to the source, so every parameter and every response status is written down as well.

Every rule of both skills is kept. Where two rules cannot both hold, `apidoc-reference-card` wins.

## Rules

- The first line must be a level-3 Markdown heading with the method and path in backticks, for example ### `GET /v1/invoices/{id}`. This is the `apidoc-reference-card` rule. It overrides the `apidoc-integrator-guide` rule that the first line is the method and path alone in plain text with no Markdown.
- State the required permission on a line `Auth: <scope>`.
- State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.
- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Show one example call, written as a shell line that starts with `$ curl `.
- Document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`.
- Keep the whole entry to at most 90 words. All the fields above have to fit inside this limit, so use one short sentence for the description and only a few words for each parameter description and each status meaning. Count the words before answering and never drop a required field to save space.

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
| id | path | string | Invoice ID |

$ curl -H "Authorization: Bearer $TOKEN" https://api.example.com/v1/invoices/inv_123

Responses:
- 200: the invoice object
- 403: scope missing
- 404: invoice not found
```
