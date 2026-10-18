---
name: sql-house-style+sql-warehouse-conventions
description: Merged skill that replaces `sql-house-style` and `sql-warehouse-conventions`. Use for any SQL query.
---

# Merged skill: sql-house-style + sql-warehouse-conventions

This skill replaces `sql-house-style` and `sql-warehouse-conventions`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `sql-house-style`

- Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`).
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.

## Rules kept unchanged from `sql-warehouse-conventions`

- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Qualify source tables with the `analytics.` schema.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.

## Reconciled rules (each one satisfies a rule of both skills at once)

- -- Purpose: <one sentence>. -- Owner: <team>

## Example

Request: Write the SQL query: revenue per country for orders created in January 2026, top 20 countries. Table orders(id, country, amount, created_at, deleted_at). Owning team: growth-analytics.

Output:

```
with base as (
  select
    country,
    amount
  from
    analytics.orders
  where
    created_at >= '2026-01-01 00:00:00'
    and created_at < '2026-02-01 00:00:00'
    and deleted_at is null
)
select
  country,
  sum(amount) as amount_sum
from
  base
group by
  country
order by
  amount_sum desc
limit 20;
```
