---
name: alert-chatops+alert-pager
description: Merged skill that replaces `alert-chatops` and `alert-pager`. Use for any on-call alert notification.
---

# Merged skill: alert-chatops + alert-pager

This skill replaces `alert-chatops` and `alert-pager`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-chatops`

- The first line must be `Alert <ID> firing on <service>`, for example `Alert ALR-7731 firing on checkout-api`.
- Tell the responder where to start on a line that begins with `First action: `.
- Describe what customers notice on a line that begins with `User impact: `.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- Give the runbook address on its own line in the form `Runbook: <url>`.

## Rules kept unchanged from `alert-pager`

- Give the measurement on a line `Value: <current> (threshold <limit>)`.
- Name the environment on a line `Env: <name>`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.

## Reconciled rules (each one satisfies a rule of both skills at once)

- **Combined Rule:** To satisfy both rules, list at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`, and ensure that the entire message, including the list, fits within 400 characters, counting spaces and line breaks. Likely causes: - - -

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
Alert ALR-7731 firing on checkout-api.
First action: Check the recent logs for any signs of increased latency or errors.
User impact: Customers may experience slow or timed-out checkout processes.
Value: 2.4 s (threshold 1.5 s).
Env: prod-eu.
For: 10m.
Likely causes:
- Increased load on the checkout-api service
- Network issues between the service and the database
- Configuration changes affecting the service's performance
Ack: reply ack ALR-7731
Runbook: https://runbooks.example.com/checkout-latency
```
