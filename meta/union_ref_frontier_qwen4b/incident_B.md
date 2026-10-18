<skill>
---
name: postmortem-lite+incident-brief
description: Combined rules of `postmortem-lite` and `incident-brief`. Use for any incident report.
---

# Combined skill: postmortem-lite + incident-brief

Follow every rule below.

## Rules from `postmortem-lite`

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Name the cause on a line that starts with `Root cause: `.

## Rules from `incident-brief`

- Describe user impact on a line that starts with `Impact: `.
- Use at most five bullet points in the whole report.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.

If two rules cannot both hold, the rule from `postmortem-lite` wins.

## Resolution of conflicting rules

The rule from `postmortem-lite` ("The first line must be `Incident <ID> - <title>`") takes precedence over the rule from `incident-brief` ("The first line must be `SEV<n>: <title>`"). Therefore, all reports must begin with `Incident <ID> - <title>`, not `SEV<n>: <title>`.

The example in the skill file has been revised to reflect this rule and to include all required elements in a compliant format.

## Revised example (must follow every rule)

Incident INC-2291 - Checkout API returned 500 errors  
Detection: Automated validation checks in staging detected incorrect output values at 16:18 UTC  
Impact: Users received inaccurate pricing estimates, leading to potential financial loss and confusion during checkout  
Duration: 54 min  
Status: resolved  
Root cause: A configuration file was misapplied during a deploy  
Action items:  
- (owner: DevOps) to implement automated configuration validation in all environments  
- (owner: Engineering) to add output validation checks to the pricing calculator service  
- (owner: SRE) to review deployment pipelines for configuration drift detection
</skill>
