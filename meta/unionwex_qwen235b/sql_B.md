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
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.

If two rules cannot both hold, the rule from `sql-warehouse-conventions` wins.

## Example

Request: Write the SQL query: revenue per country for orders created in January 2026, top 20 countries. Table orders(id, country, amount, created_at, deleted_at). Owning team: growth-analytics.

Output:

```
-- Purpose: Calculate revenue per country for orders created in January 2026, limited to top 20 countries. -- Owner: growth-analytics
with base as (
  select
    country,
    amount
  from analytics.orders
  where deleted_at is null
    and created_at >= '2026-01-01'
    and created_at < '2026-02-01'
)
select
  country,
  round(sum(amount), 2) as revenue_sum
from base
group by country
order by revenue_sum desc
limit 20
```
