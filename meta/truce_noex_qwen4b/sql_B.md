---
name: sql-warehouse-conventions+sql-house-style
description: Merged skill that replaces `sql-warehouse-conventions` and `sql-house-style`. Use for any SQL query.
---

# Merged skill: sql-warehouse-conventions + sql-house-style

This skill replaces `sql-warehouse-conventions` and `sql-house-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `sql-warehouse-conventions`

- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Qualify source tables with the `analytics.` schema.
- Put a header comment `-- Owner: <team>` at the top of the query.
- Write all SQL keywords in lowercase (`select`, `from`, `where`, `join`, `group by`, `order by`)

## Rules kept unchanged from `sql-house-style`

- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Filter date ranges with the half-open pattern `>=` start and `<` end. Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Cap the result size: every query needs a `limit` clause. Give every aggregate an alias that ends in `_cnt`, `_sum`, or `_avg`.
