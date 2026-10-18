---
name: python-combined-style
description: Write Python functions combining elements from both NumPy and Google coding styles. Use this style whenever Python code is requested.
---

# python-combined-style

This style combines elements from both NumPy and Google coding conventions to ensure clarity and consistency.

## Rules

- Start the module with `from __future__ import annotations`.
- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- State the time complexity as `Complexity: O(...)`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Annotate every parameter and the return value with type hints.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Raise `ValueError` for invalid input.
- Include at least one usage example with a `>>>` prompt in the docstring.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations

__all__ = ["compute_median"]


def compute_median(values: list[float]) -> float:
    """Return the median of a list of numbers.

    Args:
        values: The numbers to summarize.

    Returns:
        The median value.

    Complexity: O(n log n)

    Examples:
        >>> compute_median([1, 3, 2])
        2
    """
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    mid = len(ordered) // 2
    # NOTE: an even count averages the two middle values
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
```
