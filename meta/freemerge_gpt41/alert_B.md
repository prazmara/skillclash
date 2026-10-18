---
name: alert-chatops-pager
description: Write on-call alert notifications for both incident chat and pager/SMS channels. Use for any alert or paging message, following all rules for both formats.
---

# alert-chatops-pager

This skill writes alert notifications suitable for both incident chat channels and pager/SMS channels. Responders in chat must be able to start work from the alert alone, while pager messages must be concise and readable on a phone lock screen. All rules from both `alert-chatops` and `alert-pager` are enforced; where rules conflict, the `alert-chatops` rule takes precedence.

## Rules

- The first line must be `Alert <ID> firing on <service>`, for example `Alert ALR-7731 firing on checkout-api`.
- Describe what customers notice on a line that begins with `User impact: `.
- Give the runbook address on its own line in the form `Runbook: <url>`.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- Tell the responder where to start on a line that begins with `First action: `.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.
- The severity must be included in the message, in capitals, as one of `CRITICAL`, `WARNING`, or `INFO`.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
Alert ALR-7731 firing on checkout-api

Severity: CRITICAL
Value: 2.4s (threshold 1.5s)
Env: prod-eu
For: 10m
The p99 latency of checkout-api in prod-eu has been above the threshold for the last ten minutes.
User impact: customers see slow page loads during checkout and some payments time out.
First action: open the service dashboard and compare the latency curve with the last deploy marker.
Likely causes:
- A recent deploy introduced a slow database query in the order summary path.
- The payments provider is responding slowly and requests are queuing up.
- A traffic spike exhausted the database connection pool.
Runbook: https://runbooks.example.com/checkout-latency
Ack: reply ack ALR-7731
```
