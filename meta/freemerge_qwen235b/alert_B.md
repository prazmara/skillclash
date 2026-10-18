---
name: alert-notification
description: Write on-call alert notifications for both chat and pager/SMS channels. Use for any alert or paging message.
---

# alert-notification

This skill produces alert notifications suitable for both chat (e.g. incident channels) and pager/SMS (e.g. mobile notifications). The format prioritizes clarity, immediate actionability, and compatibility with both display-limited devices (like pagers) and collaborative chat environments.

## Rules

- The first line must be `Alert <ID> firing on <service>` (from `alert-chatops`).
- Immediately after, include a line `[<SEVERITY>] <service>: <summary>` (from `alert-pager`), with severity in capitals: `[CRITICAL]`, `[WARNING]`, or `[INFO]`.
- The entire message must fit on a pager screen: at most 400 characters, including spaces and line breaks (from `alert-pager`).
- Describe what customers notice on a line that begins with `User impact: ` (from `alert-chatops`).
- Give the runbook address on its own line in the form `Runbook: <url>` (from both, no conflict).
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731` (from `alert-chatops`).
- List at least three likely causes as bullets starting with `- ` under a line that reads exactly `Likely causes:` (from `alert-chatops`).
- Tell the responder where to start on a line that begins with `First action: ` (from `alert-chatops`).
- Say how long the condition has held on a line `For: <n>m`, in whole minutes (from `alert-pager`).
- Name the environment on a line `Env: <name>` (from `alert-pager`).
- Give the measurement on a line `Value: <current> (threshold <limit>)` (from `alert-pager`).
- When rules conflict, the `alert-chatops` rule takes precedence (as specified).

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
Alert ALR-7731 firing on checkout-api
[CRITICAL] checkout-api: p99 latency above threshold
Value: 2.4s (threshold 1.5s)
Env: prod-eu
For: 10m
User impact: customers see slow page loads during checkout and some payments time out.
First action: open the service dashboard and compare the latency curve with the last deploy marker.
Likely causes:
- A recent deploy introduced a slow database query in the order summary path.
- The payments provider is responding slowly and requests are queuing up.
- A traffic spike exhausted the database connection pool.
Runbook: https://runbooks.example.com/checkout-latency
Ack: reply ack ALR-7731
```
