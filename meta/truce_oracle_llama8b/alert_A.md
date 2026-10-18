---
name: alert-pager+alert-chatops
description: Merged skill that replaces `alert-pager` and `alert-chatops`. Use for any on-call alert notification.
---

# Merged skill: alert-pager + alert-chatops

This skill replaces `alert-pager` and `alert-chatops`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-pager`

- The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.
- Name the environment on a line `Env: <name>`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Link the runbook on a line `Runbook: <url>`.

## Rules kept unchanged from `alert-chatops`

- Tell the responder where to start on a line that begins with `First action: `.
- Describe what customers notice on a line that begins with `User impact: `.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- To satisfy both rules, write the message in a single line, followed by a line that reads exactly "Likely causes:", and then list at least three likely causes as bullets that start with `- ` on the same line as "Likely causes:", ensuring the whole message fits within 400 characters, counting spaces and line breaks.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: p99 latency of the checkout-api service in prod-eu is 2.4 s (threshold 1.5 s).
Value: 2.4 s (threshold 1.5 s).
Env: prod-eu.
For: 10m.
First action: Check the prod-eu cluster for any signs of resource contention or node failures.
User impact: Customers may experience slow or timed-out checkout processes.
Likely causes:
- High CPU usage on the checkout-api nodes.
- Network issues between the checkout-api and database services.
- Misconfigured load balancer rules.
Ack: reply ack ALR-7731
Runbook: https://runbooks.example.com/checkout-latency
```
