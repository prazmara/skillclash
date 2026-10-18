---
name: sql-house-warehouse
description: Write SQL that follows the data warehouse conventions and keeps the safety defaults of the analytics house style. Use for any SQL query.
---

# sql-house-warehouse

This skill merges `sql-house-style` and `sql-warehouse-conventions` and replaces both. Warehouse queries are composed from CTEs and must be attributable to an owning team. Queries are also reviewed by analysts who rely on a consistent style and on safety defaults.

Every rule of both skills is kept. Where two rules cannot both hold, `sql-warehouse-conventions` wins.

## Rules

- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Put a header comment `-- Owner: <team>` at the top of the query. It goes on the second line, directly below the purpose comment and before any SQL, so that both header rules hold.
- Write all SQL keywords in lowercase (`select`, `from`, `where`, `join`, `group by`, `order by`). This is the `sql-warehouse-conventions` rule. It overrides the `sql-house-style` rule that asks for UPPERCASE keywords, so no keyword is uppercase. The same goes for `with`, `as`, `and`, `is null`, `desc`, `limit` and for functions such as `sum` and `round`.
- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Qualify source tables with the `analytics.` schema.
- Always exclude soft-deleted rows with the filter `deleted_at is null` (the house filter `deleted_at IS NULL`, written in lowercase because of the keyword rule).
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- Wrap every monetary or averaged aggregate in `round(..., 2)` (the house rule `ROUND(..., 2)`, written in lowercase).
- Cap the result size: always end the query with a `limit` clause.

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
limit 20;
```
