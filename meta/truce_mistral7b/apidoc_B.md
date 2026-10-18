---
name: apidoc-integrator-guide+apidoc-reference-card
description: Merged skill that replaces `apidoc-integrator-guide` and `apidoc-reference-card`. Use for any REST endpoint documentation entry.
---

# Merged skill: apidoc-integrator-guide + apidoc-reference-card

This skill replaces `apidoc-integrator-guide` and `apidoc-reference-card`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `apidoc-integrator-guide`

- Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- Name the media type of the response on a line such as `Content-Type: application/json`.
- List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- Include an example request written as a shell line beginning with `$ curl `.

## Rules kept unchanged from `apidoc-reference-card`

- State the required permission on a line `Auth: <scope>`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- Show one example call on a line that starts with `$ curl `.
- Keep the whole entry to at most 90 words.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output as follows: ``` ### `GET /v1/invoices/{id}` [Method and path alone in plain text] ``` This way, the first line starts with a level-3 Markdown heading, followed by the method and path in backticks, and ends with a newline. The second line contains only the method and path alone in plain text.
- Write the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`. Indicate the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`. Arrange the output such that both rules are satisfied simultaneously.

## Example

Request: Write the documentation entry for the endpoint GET /v1/invoices/{id}: returns one invoice by ID. Requires the scope invoices:read. Path parameter id (string). Returns 200 with the invoice object, 403 if the scope is missing, 404 if the invoice does not exist. Available since API version 1.4.

Output:

```
### `GET /v1/invoices/{id}`

#### Method and path alone in plain text

#### Parameters

| Name | In | Type | Description |
|------|----|------|-------------|
| id   | path | string | The ID of the invoice to retrieve |

#### Example request

$ curl -H "Authorization: Bearer <access_token>" https://api.example.com/v1/invoices/{id}

#### Auth

invoices:read

#### Idempotent

yes

#### Example call

$ curl -H "Authorization: Bearer <access_token>" https://api.example.com/v1/invoices/12345

#### Responses:

- 200: The requested invoice was found and returned.
- 403: The provided access token does not have the required scope.
- 404: The specified invoice does not exist.

#### Stability

Stable

#### Content-Type

application/json

#### Since

v1.4
```
