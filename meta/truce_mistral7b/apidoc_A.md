---
name: apidoc-reference-card+apidoc-integrator-guide
description: Merged skill that replaces `apidoc-reference-card` and `apidoc-integrator-guide`. Use for any REST endpoint documentation entry.
---

# Merged skill: apidoc-reference-card + apidoc-integrator-guide

This skill replaces `apidoc-reference-card` and `apidoc-integrator-guide`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `apidoc-reference-card`

- State the required permission on a line `Auth: <scope>`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- Show one example call on a line that starts with `$ curl `.
- Keep the whole entry to at most 90 words.

## Rules kept unchanged from `apidoc-integrator-guide`

- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.
- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Include an example request written as a shell line beginning with `$ curl `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in two lines: 1. On the first line, use plain text and provide only the method and path: `GET /v1/invoices/{id}` 2. On the second line, use a level-3 Markdown heading with the method and path in backticks: ### `GET /v1/invoices/{id}`
- Write the output in the following format: ``` Since: v<version> Responses: - <status code>: <meaning> - <status code>: <meaning> - <status code>: <meaning> ``` Replace `<version>` with the API version that introduced the endpoint, and `<status code>` and `<meaning>` with the appropriate response status codes and their meanings.

## Example

Request: Write the documentation entry for the endpoint GET /v1/invoices/{id}: returns one invoice by ID. Requires the scope invoices:read. Path parameter id (string). Returns 200 with the invoice object, 403 if the scope is missing, 404 if the invoice does not exist. Available since API version 1.4.

Output:

```
Auth: invoices:read
Idempotent: no

$ curl -H "Authorization: Bearer <access_token>" https://api.example.com/v1/invoices/{id}

Stability: stable
Content-Type: application/json

| Name | In | Type | Description |
|------|----|------|-------------|
| id   | path | string | The ID of the invoice to retrieve |

### `GET /v1/invoices/{id}`

Since: v1.4
Responses:
- 200: The requested invoice
- 403: The scope invoices:read is missing
- 404: The invoice does not exist
```
