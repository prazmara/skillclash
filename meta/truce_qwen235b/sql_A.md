---
name: sql-house-style+sql-warehouse-conventions
description: Merged skill that replaces `sql-house-style` and `sql-warehouse-conventions`. Use for any SQL query.
---

# Merged skill: sql-house-style + sql-warehouse-conventions

This skill replaces `sql-house-style` and `sql-warehouse-conventions`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `sql-house-style`

- Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`).
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.

## Rules kept unchanged from `sql-warehouse-conventions`

- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- Qualify source tables with the `analytics.` schema.

## Reconciled rules (each one satisfies a rule of both skills at once)

- -- Owner: <team> -- Purpose: <one sentence>
- with base as (select * from source_table where deleted_at IS NULL) select * from base;

## Example

Request: Write the SQL query: revenue per country for orders created in January 2026, top 20 countries. Table orders(id, country, amount, created_at, deleted_at). Owning team: growth-analytics.

Output:

```
-- Owner: growth-analytics -- Purpose: Calculate revenue per country for orders created in January 2026, limited to top 20 countries
with base as (
    select
        country,
        amount
    from analytics.orders
    where deleted_at IS NULL
      and created_at >= '2026-01-01'
      and created_at < '2026-02-01'
)
select
    country,
    ROUND(SUM(amount), 2) as revenue_sum
from base
group by country
order by revenue_sum desc
limit 20;
```
