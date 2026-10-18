<skill>
---
name: support-friendly+support-formal
description: Merged skill that replaces `support-friendly` and `support-formal`. Use for any support reply. Follow every rule below.
---

# Merged skill: support-friendly + support-formal

This skill replaces `support-friendly` and `support-formal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-friendly`

- Invite a response with the exact phrase `reply to this email`.  
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.  
- Open with `Hi <first name>!` on the first line.

## Rules kept unchanged from `support-formal`

- Do not use contractions such as `don't`, `we'll`, or `you're`.  
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`. Give the next steps as a numbered list with at least two steps (`1.`, `2.`).  
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL and cite the case as `Ticket #<number>`.  
- Close with the agent's first name and then a line ending in `Support Team`. Sign with the agent's name followed by a line that ends with `Support Team`.

## How to satisfy all rules simultaneously

- The phrase `reply to this email` must appear **exactly once** at the beginning of the message, immediately after the greeting.  
- After the greeting, include the time frame (e.g., "We will resolve this within 2 business days") in a clear, formal statement.  
- The body must begin with either "Good news:" or "Quick update:" followed by a numbered list of at least two clear, action-oriented steps.  
- The URL and ticket number must be included **only on a final line that starts with `Links:`**, not embedded in the body.  
- All contractions (e.g., "don't", "we'll", "you're") must be avoided in all text.  
- The closing must be: the agent’s first name followed by a line ending in `Support Team`, then a second line with the agent’s full name followed by `Support Team`.

## Added clarification to satisfy both skills simultaneously

- The time frame must be explicitly stated **after the greeting**, and **before** the opening of the main message (i.e., after "Hi <first name>!", and before "Good news:" or "Quick update:").  
  Example: "We will resolve this issue within 2 business days."  
  This ensures both the time frame requirement from `support-friendly` and the formal tone from `support-formal` are met.

## Example

Request: Write the support reply to Marcus Thompson (ticket 24681): the mobile app crashes when opening the settings menu. A critical bug has been patched; uninstall and reinstall the app to apply the fix. Help article: https://help.example.com/mobile-app-crash-fix. Agent: Aria.

Output:

```
Hi Marcus!  
reply to this email  

We will resolve this issue within 2 business days.  

Good news: we have resolved the critical bug causing the mobile app to crash when opening the settings menu.  

1. Uninstall the mobile app from your device.  
2. Reinstall the app from the official app store.  

Links: https://help.example.com/mobile-app-crash-fix (Ticket #24681)  

Aria  
Support Team
```

</skill>
