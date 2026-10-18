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

- Write the output in a single line, with each bullet point separated by a single line break (`\n`). Ensure the total character count, including spaces and line breaks, is less than or equal to 400. Start the output with "Likely causes:" followed by a colon, and end with a line break. Example: ``` Likely causes:\n - Issue A\n - Issue B\n - Issue C ```

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
Alert ALR-7731 firing on checkout-api

First action: Investigate the p99 latency issue on the checkout-api service in prod-eu.
User impact: Customers may experience slow response times when using the checkout service.
Ack: reply ack ALR-7731

Likely causes:
- High traffic or load on the checkout-api service
- Database or network issues
- Code-level performance problems

Value: 2.4 s (threshold 1.5 s)
Env: prod-eu
For: 10m

Runbook: https://runbooks.example.com/checkout-latency
```
