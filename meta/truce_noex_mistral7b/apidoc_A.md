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
