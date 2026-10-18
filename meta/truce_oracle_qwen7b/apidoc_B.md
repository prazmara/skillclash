---
name: apidoc-integrator-guide+apidoc-reference-card
description: Merged skill that replaces `apidoc-integrator-guide` and `apidoc-reference-card`. Use for any REST endpoint documentation entry.
---

# Merged skill: apidoc-integrator-guide + apidoc-reference-card

This skill replaces `apidoc-integrator-guide` and `apidoc-reference-card`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `apidoc-integrator-guide`

- The first line must be the method and path alone in plain text with no Markdown, for example `GET /v1/invoices/{id}`.
- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.
- Include an example request written as a shell line beginning with `$ curl `.

## Rules kept unchanged from `apidoc-reference-card`

- State the required permission on a line `Auth: <scope>`.
- State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>` and keep the whole entry to at most 90 words.

## Example

Request: Write the documentation entry for the endpoint GET /v1/invoices/{id}: returns one invoice by ID. Requires the scope invoices:read. Path parameter id (string). Returns 200 with the invoice object, 403 if the scope is missing, 404 if the invoice does not exist. Available since API version 1.4.

Output:

```
GET /v1/invoices/{id}

| Name   | In | Type   | Description        |
|--------|----|--------|--------------------|
| id     | path | string | Invoice ID         |

Stability: stable
Content-Type: application/json
Auth: invoices:read
Since: v1.4
Idempotent: yes
Responses:
- 200: OK, returns the invoice object
- 403: Forbidden, missing scope
- 404: Not Found, invoice does not exist
```
