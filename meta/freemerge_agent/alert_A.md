---
name: alert-pager-chatops
description: Write on-call alert notifications that work on the pager and SMS channel and in the incident chat channel. Use for any alert or paging message.
---

# alert-pager-chatops

This skill merges `alert-pager` and `alert-chatops` and replaces both. One notification serves both audiences. A responder reading a phone lock screen at night must see severity, service and numbers at once, and the message must not be cut off. A responder in the chat channel must be able to start working from the alert alone, so it also says what users see, what to try and where to look.

Every rule of both skills is kept. Where two rules cannot both hold, `alert-pager` wins.

## Rules

- The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`. This is the `alert-pager` rule. It overrides the `alert-chatops` first line `Alert <ID> firing on <service>`, which is not used. The alert ID still appears in the `Ack:` line.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.
- Name the environment on a line `Env: <name>`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Describe what customers notice on a line that begins with `User impact: `.
- Tell the responder where to start on a line that begins with `First action: `.
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- Give the runbook address on its own line in the form `Runbook: <url>`.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks. Every line above has to fit inside this limit. Write each line as a short phrase of a few words, give exactly three causes unless there is clearly room for more, and add no blank lines, greetings or extra sentences. Count the characters before answering and shorten the phrases if the total is above 400. Never drop a required line to save space.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output (about 360 characters):

```
[CRITICAL] checkout-api: p99 latency above threshold
Value: 2.4s (threshold 1.5s)
Env: prod-eu
For: 10m
User impact: slow checkout, payment timeouts
First action: check latency vs last deploy
Likely causes:
- slow DB query after deploy
- payments provider slow
- DB pool exhausted
Runbook: https://runbooks.example.com/checkout-latency
Ack: reply ack ALR-7731
```
