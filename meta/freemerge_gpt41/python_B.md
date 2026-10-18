---
name: python-numpy-google-merged
description: Write Python functions in NumPy style with Google-style function naming and type hints. Use whenever Python code is requested.
---

# python-numpy-google-merged

Scientific Python code here follows NumPy conventions for documentation and module structure, and Google conventions for function naming and type hints.

## Rules

- Start the module with `from __future__ import annotations`.
- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- Annotate every parameter and the return value with type hints.
- Show a doctest-style example that uses `>>>`.
- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.
- Reject invalid input by raising `ValueError`.
- Reply with one Python code block and nothing outside it.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations

__all__ = ["compute_median"]


def compute_median(values: list[float]) -> float:
    """Return the median of a list of numbers.

    Parameters
    ----------
    values : list of float
        The numbers to summarize.

    Returns
    -------
    float
        The median value.

    Examples
    --------
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

Complexity: O(n log n)
