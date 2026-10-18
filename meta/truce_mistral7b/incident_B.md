---
name: postmortem-lite+incident-brief
description: Merged skill that replaces `postmortem-lite` and `incident-brief`. Use for any incident report.
---

# Merged skill: postmortem-lite + incident-brief

This skill replaces `postmortem-lite` and `incident-brief`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `postmortem-lite`

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- Name the cause on a line that starts with `Root cause: `.

## Rules kept unchanged from `incident-brief`

- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: `Incident <ID> - <title>\nImpact: <description of user impact>` For example: `Incident INC-2291 - Checkout API returned 500 errors\nImpact: The Checkout API is experiencing issues, causing some users to encounter errors during the checkout process.`
- Write the output in the following format: "Detection: [Time in 24-hour HH:MM UTC format] - [Detailed description of the problem]". For example, "Detection: 09:14 UTC - Unexpected system error occurred in module X".
- Write the output as follows: "Incident Brief: Duration: <n> min" This way, the length of the incident is reported on a separate line with the label "Duration", satisfying both rules from the `postmortem-lite` and `incident-brief` skills.
- Write the output in the following format: ``` Status: investigating Action items: - (owner: <team1>) - Action 1 - (owner: <team2>) - Action 2 - (owner: <team3>) - Action 3 ```

## Example

Request: Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.

Output:

```
SEV2: Checkout API returned 500 errors
Incident INC-2291 - Checkout API returned 500 errors
Impact: The Checkout API is experiencing issues, causing some users to encounter errors during the checkout process.

Detection: 09:14 UTC - Unexpected system error occurred in the Checkout API

Incident Brief: Duration: 42 min

Status: investigating
Action items:
- (owner: DevOps) - Investigate the root cause of the TLS certificate expiration
- (owner: SRE) - Implement a monitoring solution to detect certificate expirations in advance
- (owner: Security) - Renew the TLS certificate for the payments gateway and ensure proper renewal procedures are in place
```
