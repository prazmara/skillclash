# Skill pairs for the human check

For each job, two skills A and B do the same job. Rules are numbered in the order they appear in the skill files.

## commit (commit message)

**Skill A: `conventional-commits`**

- A1. Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- A2. Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- A3. Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- A4. State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- A5. The very last line of the message must be the sign-off `Signed-off-by: <author name>`.
- A6. Explain the motivation in a body line that starts with `Why: `.

**Skill B: `ticket-first-commits`**

- B1. Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.
- B2. Record test status as `Tested: yes` or `Tested: no` on its own line.
- B3. Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- B4. Say how to revert in a line that starts with `Rollback: `.
- B5. Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
- B6. Name the affected component in a line `Component: <name>`.

## pr (pull request description)

**Skill A: `pr-structured`**

- A1. Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.
- A2. Include a section with the exact heading `## Testing`.
- A3. Give the tracker ticket on its own line as `Ticket: <ID>`.
- A4. Include a section with the exact heading `## Summary`.
- A5. The first line must be a level-1 Markdown heading with the title, starting with `# `.
- A6. Keep the whole description to at most 120 words.

**Skill B: `pr-release-ready`**

- B1. List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.
- B2. Put the ticket on a separate line in the form `Ticket: <ID>`.
- B3. Name the reviewers on a line `Reviewers: @handle`.
- B4. The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.
- B5. Include a section with the exact heading `## Rollback`.
- B6. Include a `## Risks` section with at least two bullet points that start with `- `.

## sql (SQL query)

**Skill A: `sql-house-style`**

- A1. Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- A2. Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`).
- A3. Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- A4. The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- A5. Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- A6. Always end the query with a `LIMIT` clause.

**Skill B: `sql-warehouse-conventions`**

- B1. Cap the result size: every query needs a `limit` clause.
- B2. Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- B3. Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- B4. Qualify source tables with the `analytics.` schema.
- B5. Put a header comment `-- Owner: <team>` at the top of the query.
- B6. Write all SQL keywords in lowercase (`select`, `from`, `where`, `join`, `group by`, `order by`).

## incident (incident report)

**Skill A: `incident-brief`**

- A1. Describe user impact on a line that starts with `Impact: `.
- A2. Use at most five bullet points in the whole report.
- A3. Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- A4. State the length of the incident on a line `Duration: <n> min`.
- A5. Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- A6. The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.

**Skill B: `postmortem-lite`**

- B1. Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- B2. The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- B3. Say how the problem was noticed on a line that starts with `Detection: `.
- B4. Report how long the incident lasted as `Duration: <n> min` on its own line.
- B5. End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- B6. Name the cause on a line that starts with `Root cause: `.

## python (Python function)

**Skill A: `python-google-style`**

- A1. Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- A2. Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- A3. Annotate every parameter and the return value with type hints.
- A4. Reject invalid input by raising `ValueError`.
- A5. Include at least one usage example with a `>>>` prompt in the docstring.
- A6. Reply with one Python code block and nothing outside it.

**Skill B: `python-numpy-style`**

- B1. Start the module with `from __future__ import annotations`.
- B2. Show a doctest-style example that uses `>>>`.
- B3. State the time complexity as `Complexity: O(...)`.
- B4. Export the function by defining `__all__`.
- B5. Mark each non-obvious step with a comment that starts with `# NOTE:`.
- B6. Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.

## support (support reply)

**Skill A: `support-formal`**

- A1. Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- A2. Cite the case as `Ticket #<number>`.
- A3. Open with `Dear <full name>,` on the first line.
- A4. Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- A5. Sign with the agent's name followed by a line that ends with `Support Team`.
- A6. Do not use contractions such as `don't`, `we'll` or `you're`.

**Skill B: `support-friendly`**

- B1. Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- B2. Invite a response with the exact phrase `reply to this email`.
- B3. Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- B4. Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- B5. Open with `Hi <first name>!` on the first line.
- B6. Close with the agent's first name and then a line ending in `Support Team`.

## changelog (changelog entry)

**Skill A: `keep-a-changelog`**

- A1. Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.
- A2. Flag incompatible changes with the exact marker `BREAKING:`.
- A3. Reference issues in parentheses as `(#<number>)`.
- A4. Bullets describe the change only. No bullet may contain an @handle.
- A5. The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.
- A6. Bullets are fragments: no bullet may end with a period.

**Skill B: `release-announcement`**

- B1. The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`.
- B2. Open with a one-sentence summary on a line that starts with `Highlights: `.
- B3. Credit every contributor by @handle.
- B4. Mark incompatible changes with `BREAKING:` exactly.
- B5. Tell users what to do on a line that starts with `Upgrade: `.
- B6. Put the name of each new feature in bold with `**`.

## apierror (JSON error response body)

**Skill A: `api-errors-internal`**

- A1. The reply must be exactly one JSON object and nothing else, so that it parses as JSON.
- A2. Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.
- A3. Include a human-readable sentence in the field `message`.
- A4. Include a boolean field `retryable`.
- A5. Include the HTTP status as an integer in the field `status`.
- A6. Include a field `docs` with an `https://` link to the error documentation.

**Skill B: `api-errors-public`**

- B1. Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.
- B2. Include a field `severity` with the value `low`, `medium` or `high`.
- B3. Include a field `details` that holds a non-empty list of specifics.
- B4. Add a developer hint that starts with `Hint:` and says how to fix the request.
- B5. Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.
- B6. Explain the error for humans in the `message` field.

## review (code review comment)

**Skill A: `review-triage`**

- A1. The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.
- A2. Propose the change on a line that starts with `Proposed fix: `.
- A3. Give the place in the code on its own line as `Location: <file>:<line>`.
- A4. Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- A5. State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.
- A6. Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.

**Skill B: `review-mentoring`**

- B1. Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.
- B2. Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.
- B3. The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.
- B4. Name one good thing about the diff on a line that starts with `What works well: `.
- B5. Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.
- B6. Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.

## testcase (test case specification)

**Skill A: `testcase-compact`**

- A1. Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- A2. The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- A3. State the pass criterion on a line that starts with `Expected result: `.
- A4. Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- A5. Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- A6. Describe the starting state on a line that begins with `Preconditions: `.

**Skill B: `testcase-traceable`**

- B1. Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- B2. List the data the tester needs on a line that starts with `Test data: `.
- B3. Link the feature under test on a line `Covers: <feature>`.
- B4. Write the outcome that counts as a pass on its own line beginning with `Expected result: `.
- B5. Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`
- B6. The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## standup (daily standup update)

**Skill A: `standup-async-thread`**

- A1. Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- A2. List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- A3. The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- A4. Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
- A5. List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- A6. The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.

**Skill B: `standup-manager-digest`**

- B1. The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.
- B2. Summarize the workload on a line `Items: <n> done, <n> planned`.
- B3. Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- B4. Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.
- B5. Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- B6. Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.

## bugreport (bug report)

**Skill A: `bug-triage-form`**

- A1. Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.
- A2. Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.
- A3. The first line must be plain text of the form `Title: <one-line summary>`.
- A4. Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.
- A5. Give the app version and the platform on one line that starts with `Environment: `.
- A6. Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.

**Skill B: `bug-dev-handoff`**

- B1. The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`.
- B2. Name the person who found the bug on a line `Reported by: <full name>`.
- B3. Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.
- B4. Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.
- B5. Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.
- B6. Quote the exact error message inside backticks so that developers can search for it.

## dockerfile (Dockerfile)

**Skill A: `dockerfile-hardened`**

- A1. The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- A2. Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.
- A3. Declare a `HEALTHCHECK` instruction that probes the service.
- A4. Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- A5. Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.
- A6. Set the working directory with `WORKDIR /opt/service`. No other working directory may be used anywhere in the file.

**Skill B: `dockerfile-catalog`**

- B1. Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.
- B2. Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.
- B3. Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- B4. Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- B5. Put a header comment `# Owner: <team>` at the top of the file.
- B6. Fix the container time zone with `ENV TZ=UTC`.

## apidoc (REST endpoint documentation entry)

**Skill A: `apidoc-reference-card`**

- A1. State the required permission on a line `Auth: <scope>`.
- A2. Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- A3. Show one example call on a line that starts with `$ curl `.
- A4. The first line must be a level-3 Markdown heading with the method and path in backticks, for example ### `GET /v1/invoices/{id}`.
- A5. Keep the whole entry to at most 90 words.
- A6. State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.

**Skill B: `apidoc-integrator-guide`**

- B1. The first line must be the method and path alone in plain text with no Markdown, for example `GET /v1/invoices/{id}`.
- B2. Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.
- B3. Name the media type of the response on a line such as `Content-Type: application/json`.
- B4. List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.
- B5. Include an example request written as a shell line beginning with `$ curl `.
- B6. Document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`.

## alert (on-call alert notification)

**Skill A: `alert-pager`**

- A1. Link the runbook on a line `Runbook: <url>`.
- A2. The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- A3. The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- A4. Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- A5. Name the environment on a line `Env: <name>`.
- A6. Give the measurement on a line `Value: <current> (threshold <limit>)`.

**Skill B: `alert-chatops`**

- B1. The first line must be `Alert <ID> firing on <service>`, for example `Alert ALR-7731 firing on checkout-api`.
- B2. Describe what customers notice on a line that begins with `User impact: `.
- B3. Give the runbook address on its own line in the form `Runbook: <url>`.
- B4. Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- B5. List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- B6. Tell the responder where to start on a line that begins with `First action: `.

## userstory (user story ticket)

**Skill A: `story-portfolio`**

- A1. Say what the story does not cover on a line that starts with `Out of scope: `.
- A2. The line directly below the title must be `Epic: <epic name>`.
- A3. The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- A4. Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- A5. Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- A6. List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

**Skill B: `story-sprint-ready`**

- B1. Name who the story is for on a line `Persona: <persona>`.
- B2. Put the estimate at the top, right under the title, as `Story points: <n>`.
- B3. Say how success will be measured on a line that starts with `Metric: `.
- B4. Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- B5. List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.
- B6. The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.
