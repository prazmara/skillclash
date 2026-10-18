---
name: alert-pager+alert-chatops
description: Merged skill that replaces `alert-pager` and `alert-chatops`. Use for any on-call alert notification.
---

# Merged skill: alert-pager + alert-chatops

This skill replaces `alert-pager` and `alert-chatops`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-pager`

- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.

## Rules kept unchanged from `alert-chatops`

- Describe what customers notice on a line that begins with `User impact: `
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the runbook URL on a separate line, ensuring it is formatted as follows: Runbook: <url> This format will satisfy both the rules from the skills `alert-pager` and `alert-chatops`.
- Write the output in the following format: "<[SEVERITY]> <Alert ID> on <service>: <summary>" For example: "[CRITICAL] ALR-7731 on checkout-api: Critical error detected in checkout process" This way, the first line satisfies both the rules from the `alert-pager` and `alert-chatops` skills.
- Write the output in the following format: "First action: For <n>m minutes, the condition has held."

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
"[CRITICAL] ALR-7731 on checkout-api: p99 latency of 2.4 s in prod-eu, above the 1.5 s threshold, for 10 minutes.
First action: For 10 minutes, the condition has held.

Env: prod-eu
Value: 2.4 s (threshold 1.5 s)

User impact: Customers may experience slow checkout times.
Ack: reply ack ALR-7731

Likely causes:
- Increased traffic to the checkout-api service
- Resource contention on the server hosting the checkout-api service
- Issues with the database connection to the checkout-api service

Runbook: https://runbooks.example.com/checkout-latency"
```
