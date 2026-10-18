<skill>
---
name: sql-warehouse-style
description: Write SQL in the analytics warehouse style. Use for any SQL query.
---

# sql-warehouse-style

Queries are reviewed by analysts who rely on a consistent style and on safety defaults.

## Rules

- Cap the result size: every query needs a `LIMIT` clause.
- Stage the source rows in a CTE named `base` (`WITH base AS (...)`) and select from it.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `BETWEEN` or `<=` for dates.
- Qualify source tables with the `analytics.` schema.
- Put a header comment `-- Owner: <team>` at the top of the query.
- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Write all SQL keywords in lowercase (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`).
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.

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
    where o.deleted_at IS NULL
      and o.created_at >= '2026-01-01'
      and o.created_at < '2026-02-01'
)
select
    country,
    ROUND(SUM(amount), 2) AS revenue_sum
from base
group by country
order by revenue_sum DESC
limit 20;
```
