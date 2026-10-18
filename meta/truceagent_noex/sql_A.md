---
name: sql-house-style+sql-warehouse-conventions
description: Merged skill that replaces `sql-house-style` and `sql-warehouse-conventions`. Use for any SQL query.
---

# Merged skill: sql-house-style + sql-warehouse-conventions

This skill replaces `sql-house-style` and `sql-warehouse-conventions`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `sql-house-style`

- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`).
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.

## Rules kept unchanged from `sql-warehouse-conventions`

- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- Qualify source tables with the `analytics.` schema.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`. Put the header comment `-- Owner: <team>` on the second line, directly below the purpose comment and above the first line of SQL, so that both comments sit at the top of the query.
