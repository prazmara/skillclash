---
name: alert-chatops+alert-pager
description: Merged skill that replaces `alert-chatops` and `alert-pager`. Use for any on-call alert notification.
---

# Merged skill: alert-chatops + alert-pager

This skill replaces `alert-chatops` and `alert-pager`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-chatops`

- Give the runbook address on its own line in the form `Runbook: <url>`.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- Tell the responder where to start on a line that begins with `First action: `.

## Rules kept unchanged from `alert-pager`

- Link the runbook on a line `Runbook: <url>`.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Alert <ID> firing on <service> On a separate line, write `Env: <name>`.
- To satisfy both rules, arrange the output so that the line starting with "User impact: " contains the measurement and the line starting with "Value: " contains the threshold, and format the line starting with "Value: " as "Value: <current> (threshold <limit>)".

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
Env: prod-eu
Alert ALR-7731 firing on checkout-api
User impact: High p99 latency
Value: 2.4 s (threshold 1.5 s)
For: 10m
Severity: Critical
Likely causes:
- High CPU usage on checkout-api
- Network congestion between checkout-api and database
- Misconfigured load balancer
First action: Check the CPU usage and network latency of checkout-api
Runbook: https://runbooks.example.com/checkout-latency
Ack: reply ack ALR-7731
```
