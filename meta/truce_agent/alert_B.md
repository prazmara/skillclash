---
name: alert-chatops+alert-pager
description: Merged skill that replaces `alert-chatops` and `alert-pager`. Use for any on-call alert notification.
---

# Merged skill: alert-chatops + alert-pager

This skill replaces `alert-chatops` and `alert-pager`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-chatops`

- The first line must be `Alert <ID> firing on <service>`, for example `Alert ALR-7731 firing on checkout-api`.
- Describe what customers notice on a line that begins with `User impact: `.
- Give the runbook address on its own line in the form `Runbook: <url>`.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- Tell the responder where to start on a line that begins with `First action: `.

## Rules kept unchanged from `alert-pager`

- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- List exactly three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`, and keep each cause to a phrase of at most four words. The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks, so keep every other line to one short phrase as well.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
Alert ALR-7731 firing on checkout-api
Value: 2.4s (threshold 1.5s)
Env: prod-eu
For: 10m
User impact: checkout is slow for customers
First action: check the service dashboard
Likely causes:
- slow database query
- slow payments provider
- exhausted connection pool
Runbook: https://runbooks.example.com/checkout-latency
Ack: reply ack ALR-7731
```
