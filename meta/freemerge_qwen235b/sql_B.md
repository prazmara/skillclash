---
name: sql-warehouse-conventions
description: Write SQL that follows the data warehouse conventions and house style. Use for any SQL query.
---

# sql-warehouse-conventions

Warehouse queries are composed from CTEs, must be attributable to an owning team, and follow a consistent style for readability and safety.

## Rules

- Cap the result size: every query needs a `limit` clause.
- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- Qualify source tables with the `analytics.` schema.
- Put a header comment `-- Owner: <team>` at the top of the query.
- Write all SQL keywords in lowercase (`select`, `from`, `where`, `join`, `group by`, `order by`).
- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.

## Example

Request: Write the SQL query: revenue per country for orders created in January 2026, top 20 countries. Table orders(id, country, amount, created_at, deleted_at). Owning team: growth-analytics.

Output:

```
-- Purpose: revenue per country for January 2026
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
