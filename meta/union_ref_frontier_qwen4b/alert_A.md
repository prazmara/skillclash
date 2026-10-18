<skill>
---
name: alert-pager+alert-chatops
description: Combined rules of `alert-pager` and `alert-chatops`. Use for any on-call alert notification.
---

# Combined skill: alert-pager + alertops

Follow every rule below.

## Rules from `alert-pager`

- Link the runbook on a line `Runbook: <url>`.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.

## Rules from `alert-chatops`

- The first line must be `Alert <ID> firing on <service>`, for example `Alert ALR-7731 firing on checkout-api`.
- Describe what customers notice on a line that begins with `User impact:`.
- Give the runbook address on its own line in the form `Runbook: <url>`.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- Tell the responder where to start on a line that begins with `First action:`.

## Conflict Resolution

If two rules cannot both hold, the rule from `alert-pager` wins.  
Specifically:
- The first line must be `[<SEVERITY>] <service>: <summary>` (from `alert-pager`), **not** `Alert <ID> firing on <service>` (from `alert-chatops`).  
- The runbook link must appear exactly once and on a line `Runbook: <url>`, as required by both rules — this is satisfied by the `alert-pager` version.  
- The `Value: <current> (threshold <limit>)` line is required by `alert-pager` and must be present; it takes precedence over any omission in `alert-chatops`.  
- The `For: <n>m` and `Env: <name>` lines are required by `alert-pager` and must be included.  
- The `User impact:` line is optional in `alert-pager` but not in `alert-chatops`; however, since `alert-pager` does not require it, and `alert-chatops` does, **both are required** — but the `alert-pager` rules take precedence **only when conflicting**. Since the user impact line does not conflict in structure or content, it is **retained** as part of the combined rules.  
- The `Likely causes:` and `First action:` lines are required by `alert-chatops` and are **retained** as long as they do not violate the character limit or conflict with `alert-pager` rules.

## Final Rule Set (All Must Be Satisfied)

1. The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
2. The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
3. Say how long the condition has held on a line `For: <n>m`, in whole minutes.
4. Name the environment on a line `Env: <name>`.
5. Give the measurement on a line `Value: <current> (threshold <limit>)`.
6. Describe what customers notice on a line that begins with `User impact:`.
7. Give the runbook address on its own line in the form `Runbook: <url>`.
8. Explain how to acknowledge with the line `Ack: reply ack <alert ID>`.
9. List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
10. Tell the responder where to start on a line that begins with `First action:`.

## Character Counting and Formatting Notes

- All lines must be formatted exactly as specified: no extra spaces, no line breaks within lines, no deviation in capitalization or punctuation.
- Line breaks are counted in the total character limit (including spaces).
- The `Likely causes:` line must appear exactly once and be immediately followed by at least three bullet points starting with `- `.
- The `First action:` line must appear exactly once and start with the prefix `First action: `.
- The `User impact:` line must appear exactly once and start with the prefix `User impact: `.
- The message must not exceed 400 characters in total, including all spaces and line breaks.

## Example (Valid Output)

[WARNING] auth-service: session timeout duration 180s above 60s threshold  
For: 13m  
Env: prod-apac  
Value: 180s (threshold 60s)  
User impact: Users may be logged out unexpectedly during prolonged inactivity.  
Runbook: https://runbooks.example.com/auth-session-timeout  
Ack: reply ack ALR-7744  
Likely causes:  
- Configuration drift due to recent deployments  
- Misconfigured session timeout settings in the auth-service  
- Network latency causing delayed session validation  
First action: Verify the current session timeout configuration in the auth-service
