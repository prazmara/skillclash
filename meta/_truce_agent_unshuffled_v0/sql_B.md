---
name: sql-warehouse-conventions+sql-house-style
description: Merged skill that replaces `sql-warehouse-conventions` and `sql-house-style`. Use for any SQL query.
---

# Merged skill: sql-warehouse-conventions + sql-house-style

This skill replaces `sql-warehouse-conventions` and `sql-house-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `sql-warehouse-conventions`

- Write all SQL keywords in lowercase (`select`, `from`, `where`, `join`, `group by`, `order by`).
- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Qualify source tables with the `analytics.` schema.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- Cap the result size: every query needs a `limit` clause.

## Rules kept unchanged from `sql-house-style`

- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`. Put the header comment `-- Owner: <team>` on the second line, directly below the purpose comment and above the first line of SQL, so that both comments sit at the top of the query.

## Example

Request: Write the SQL query: revenue per country for orders created in January 2026, top 20 countries. Table orders(id, country, amount, created_at, deleted_at). Owning team: growth-analytics.

Output:

```
-- Purpose: January 2026 revenue per country, top 20 countries
-- Owner: growth-analytics
with base as (
    select
        o.country,
        o.amount
    from analytics.orders as o
    where o.deleted_at is null
      and o.created_at >= '2026-01-01'
      and o.created_at < '2026-02-01'
)
select
    country,
    round(sum(amount), 2) as revenue_sum
from base
group by country
order by revenue_sum desc
limit 20
```
