<skill>
---
name: combined-alert
description: Write on-call alert notifications for the incident chat channel and pager/SMS. Use for any alert or paging message.
---

# combined-alert

This skill combines the functionality of writing alert notifications for both the incident chat channel and pager/SMS. For the chat channel, responders should be able to start working from the alert alone, while for the pager, the message must fit on a screen and include all necessary details succinctly.

## Rules

- **Chat Channel:**
  - The first line must be `Alert <ID> firing on <service>`, for example `Alert ALR-7731 firing on checkout-api`.
  - Describe what customers notice on a line that begins with `User impact: `.
  - Give the runbook address on its own line in the form `Runbook: <url>`.
  - Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
  - List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
  - Tell the responder where to start on a line that begins with `First action: `.

- **Pager:**
  - Link the runbook on a line `Runbook: <url>`.
  - The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
  - The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
  - Say how long the condition has held on a line `For: <n>m`, in whole minutes.
  - Name the environment on a line `Env: <name>`.
  - Give the measurement on a line `Value: <current> (threshold <limit>)`.

Where two rules cannot both hold, the rule from `alert-chatops` wins.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: p99 latency above threshold
Value: 2.4s (threshold 1.5s)
Env: prod-eu
For: 10m
Runbook: https://runbooks.example.com/checkout-latency

Alert ALR-7731 firing on checkout-api

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
</skill>
