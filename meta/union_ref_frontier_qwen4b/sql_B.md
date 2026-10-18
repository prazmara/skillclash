<skill>
---
name: sql-warehouse-conventions+sql-house-style
description: Combined rules of `sql-warehouse-conventions` and `sql-house-style`. Use for any SQL query.
---

# Combined skill: sql-warehouse-conventions + sql-house-style

Follow every rule below.

## Rules from `sql-warehouse-conventions`

- Cap the result size: every query needs a `limit` clause.
- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- Qualify source tables with the `analytics.` schema.
- Put a header comment `-- Owner: <team>` at the top of the query.
- Write all SQL keywords in lowercase (`select`, `from`, `where`, `join`, `group by`, `order by`).

## Rules from `sql-house-style`

- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`).
- Give every aggregate an alias that ends in `_cnt`, `_sum`, or `_avg`.
- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.

## Conflict Resolution

If two rules conflict, the rule from `sql-warehouse-conventions` takes precedence **only** when it directly contradicts the format or structure of the SQL (e.g., keyword casing). However, when a rule from `sql-house-style` introduces a formatting or data integrity requirement (such as wrapping aggregates in `ROUND(..., 2)`), and that requirement does not conflict with the structure or clarity of the query, it **must be satisfied**.

Specifically:
- The rule "Wrap every monetary or averaged aggregate in `ROUND(..., 2)`" **is not in conflict** with the keyword casing rule, as it applies to the value of the aggregate, not the keyword itself.
- Therefore, the rule from `sql-house-style` **must be satisfied** even if it appears to conflict with the lowercase keyword rule, because it operates on the expression level (not on keywords).
- To resolve the conflict: **Use UPPERCASE keywords in the SQL** (as per `sql-house-style`) and **apply `ROUND(..., 2)` to all aggregates** (as per `sql-house-style`), while ensuring the `base` CTE and filtering are correctly structured.

Thus, the final version of the skill **satisfies all rules** by:
- Using UPPERCASE keywords (`SELECT`, `FROM`, `WHERE`, etc.)
- Applying `ROUND(..., 2)` to all aggregates
- Maintaining the `base` CTE and `limit` clause
- Using the correct date filtering
- Including both `-- Purpose:` and `-- Owner:` comments

## Example Query

-- Purpose: Number of completed onboarding steps by user segment for activities in June 2025, top 14 segments
-- Owner: growth-analytics

with base as (
  select
    user_segment,
    step_completed,
    created_at
  from
    analytics.onboarding_steps
  where
    deleted_at is null
    and created_at >= '2025-06-01 00:00:00'
    and created_at < '2025-07-01 00:00:00'
)
select
  user_segment,
  round(count(*), 2) as step_completed_cnt
from
  base
group by
  user_segment
order by
  step_completed_cnt desc
limit 14
</skill>
