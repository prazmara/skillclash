---
name: alert-chatops+alert-pager
description: Merged skill that replaces `alert-chatops` and `alert-pager`. Use for any on-call alert notification.
---

# Merged skill: alert-chatops + alert-pager

This skill replaces `alert-chatops` and `alert-pager`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-chatops`

- Describe what customers notice on a line that begins with `User impact: `
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`

## Rules kept unchanged from `alert-pager`

- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format, ensuring both rules are satisfied: "Runbook: <url>\n(Link: Runbook: <url>)"
- Write the output as follows: `[CRITICAL] checkout-api: Alert ALR-7731 firing on checkout-api`
- Write the output in the following format: "First action: <perform action> For: <duration in whole minutes>"

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] prod-eu: Alert ALR-7731 firing on checkout-api

User impact: The p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes.

Env: prod-eu

Value: 2.4 s (threshold 1.5 s)

Likely causes:
- Increased traffic to the checkout-api service
- Database or network issues
- Code changes causing performance degradation

First action: Investigate the cause of the high latency and take corrective action. For: 30 minutes

Runbook: https://runbooks.example.com/checkout-latency

Ack: reply ack ALR-7731
```
